# products                              sales
#
# +------------------+---------+        +------------------+---------+
#
# | product_id       | int     |------->| product_id       | int     |
#
# | product_class_id | int     |  +---->| store_id         | int     |
#
# | brand_name       | varchar |  |  +->| customer_id      | int     |
#
# | product_name     | varchar |  |  |  | promotion_id     | int     |
#
# | price            | int     |  |  |  | store_sales      | decimal |
#
# +------------------+---------+  |  |  | store_cost       | decimal |
#
#                                 |  |  | units_sold       | decimal |
#
#                                 |  |  | transaction_date | date    |
#
#                                 |  |  +------------------+---------+
#
#                                 |  |
#
# stores                          |  |  customers
#
# +-------------------+---------+ |  |  +---------------------+---------+
#
# | store_id          | int     |-+  +--| customer_id         | int     |
#
# | type              | varchar |       | first_name          | varchar |
#
# | name              | varchar |       | last_name           | varchar |
#
# | state             | varchar |       | state               | varchar |
#
# | first_opened_date | datetime|       | birthdate           | date    |
#
# | last_remodel_date | datetime|       | education           | varchar |
#
# | area_sqft         | int     |       | gender              | varchar |
#
# +-------------------+---------+       | date_account_opened | date    |
#
#                                       +---------------------+---------+


# What brands have an average price above $3 and contain at least 2 different products?

select brand_name
from brands
group by brand_name
having avg(brand_name) > 3 and count(distinct product_id) >= 2 ;


#   To improve sales, the marketing department runs various types of promotions.
#   The marketing manager would like to analyze the effectiveness of these promotion campaigns.
#   In particular, what percent of our sales transactions had a valid promotion applied?
#

select sum(case when promotion_id is not null then 1 else 0)/ count(1) * 100
from sales

#   We want to run a new promotion for our most successful category of products
#   (we call these categories “product classes”).
#   Can you find out what are the top 3 selling product classes by total sales?

select product_id
from products pd join sales s on s.product_id = pd.product_id
group by sum(unit_sold*store_sales) limit 3


# We are considering running a promo across brands. We want to target
#     customers who have bought products from two specific brands.
#     Can you find out which customers have bought products from both the
#     “Fort West" and the "Golden" brands?

select customer_id , count(distinct  brandname) from
product pd join sales s on pd.product_id = s.product_id
where brand_name in ('Fort West', 'Golden')
group by customer_id having count(distinct brandname ) = 2

#
#     find sum of unit sold for each product class
# the ratio of unit_sold with valid promotion /without valid promotion
#     result should in increasing order of total_cost

