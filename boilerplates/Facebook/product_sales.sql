sales
+------------------+---------
| product_id | INTEGER
| store_id | INTEGER |
| customer_id | INTEGER |
| promotion_id | INTEGER |
| store_sales | DECIMAL |
| store_cost | DECIMAL |
| units_sold | DECIMAL |
| transaction_date | DATE |

products
+------------------+---------
| product_id | INTEGER |
| product_class_id | INTEGER |
| brand_name | VARCHAR |
| product_name | VARCHAR |
| is_low_fat_flg | TINYINT |
| is_recyclable_flg | TINYINT |
| gross_weight | DECIMAL |
| net_weight | DECIMAL |

promotions |
+------------------+---------+
| promotion_id | INTEGER|
| promotion_name | VARCHAR |
| media_type | VARCHAR |
| cost | DECIMAL |
| start_date | DATE |
| end_date | DATE |

product_classes
+------------------+---------+
| product_class_id | INTEGER |
| product_subcategory | VARCHAR |
| product_category | VARCHAR |
| product_department | VARCHAR |
| product_family | VARCHAR |

#
# What percent of all products in the grocery chain's catalog are both low fat and recyclable?

with flag_total as (
    Select
        SUM (CASE when is_low_fat_flg =1 and is_recyclable_flg =1 then 1 else 0 end) as flag_count,
        count(distinct product_id) as prod_count
   from products
 )
select
            flag_count/ prod_count * 100 as percent
from flag_total


# Q2. find top 5 sales products having promotions

select product_id
from sales
where promotion_id is not null
group by product_id
order by sum(units_sold * store_sales) desc
limit 5

#
# Q3. Percent of sales that had a valid promotion, the VP of marketing wants to
# know what percent of transactions occur on either the very first day or the very last day of a
# promotion campaign.

    SELECT ROUND(SUM(CASE WHEN s.transaction_date in(p.start_date, p.end_Date) THEN 1 ELSE 0 END)* 100/count(), 2)
    FROM sales s
        LEFT JOIN p
    ON s.promotion_id=p.promotion_id

#  Q4. Which product had the highest sales with promotions and sales
#  ( basically a where clause on 2 flags)
    SELECT
        product_id, sum(store_sales) as total_sales
    FROM
        Sales
    WHERE
        promotion_id is not null
    GROUP BY 1
    ORDER BY 2 desc
    LIMIT 1

#
#  Q5. What are the top five (ranked in decreasing order) single-channel media types that
#  correspond to the most money the grocery chain had spent on its promotional campaigns?
#  media_type can contain mutliple values seperated by a comma,
#  so single channel is when media_type only has one value.

    SELECT media_type, SUM(cost) FROM (
                                          SELECT DISTINCT media_type, s.promotion_id, cost
                                          FROM promotions p
                                                   JOIN sales s
                                                        ON p.promotion_id = s.promotion_id
                                                   JOIN products pd
                                                        ON pd.product_id = s.product_id
                                                   JOIN product_classes pc
                                                        ON pc.product_class_id = pd.product_class_id
                                          WHERE s.promotion_id > 0
                                            AND media_type NOT LIKE "%,%"
                                            AND product_department = "grocery"
                                      ) t
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 5;

#
#     Q6. the proportion of valid sales that occurred on certain dates.

    select sum(case when transaction_date = 'certain_date' then 1 end)/count(*)
    from sales
    where transaction_date is not null
#
#     Q7. Manager want to analyze the how the promotions on certain products are
#     performing.find how the the percent of promoted sales?

    with prom_sale
    as
    (select
        product_id,
        sum(store_sales) as prom_sale
    from product prod
    join promotions prom
    on  prod.promotion_id = prom.promotion_id),
    tot_sale as (
    select
        product_id,
        sum(store_sales) as tot_sale
    from product prod
    )
    select
        product_id,
        prom_sale/tot_sale * 100
    from prom_sale ps
             join tot_sale ts
                  on ps.product_id = ts.product_id
    where ps.product_id = 'certain product'

#
#     Q8. Get the top3 product class_id by the total sales.

    select product_class_id
    from product join sales on product_id
    order by sum(units_sold * store_sales) desc
    limit 3
#
#     Write a query that returns product_family, units_sold, percentage of promoted.

select
    product_family , sum(s.units_sold),
      sum (case when s.promotion_id is not null then 1 else 0) / count(1) * 100
    sales s join product pd on s.product_id = pd.product_id
    join product_classes pc on pd.product_class_id = pc.product_class_id