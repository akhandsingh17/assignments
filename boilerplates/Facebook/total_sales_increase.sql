
# +-------------------+-------------+------+-----+---------+-------+
# | Field             | Type        | Null | Key | Default | Extra |
# +-------------------+-------------+------+-----+---------+-------+
# | store_id          | int         | NO   | PRI | NULL    |       |
# | type              | varchar(30) | YES  |     | NULL    |       |
# | name              | varchar(30) | YES  |     | NULL    |       |
# | state             | varchar(30) | YES  |     | NULL    |       |
# | first_opened_date | datetime    | YES  |     | NULL    |       |
# | last_remodel_date | datetime    | YES  |     | NULL    |       |
# | area_sqft         | int         | YES  |     | NULL    |       |
# +-------------------+-------------+------+-----+---------+-------+
# mysql> describe sales;
# +------------------+---------------+------+-----+---------+-------+
# | Field            | Type          | Null | Key | Default | Extra |
# +------------------+---------------+------+-----+---------+-------+
# | product_id       | int           | NO   | MUL | NULL    |       |
# | store_id         | int           | NO   | MUL | NULL    |       |
# | customer_id      | int           | NO   | MUL | NULL    |       |
# | promotion_id     | int           | NO   |     | NULL    |       |
# | store_sales      | decimal(10,4) | NO   |     | NULL    |       |
# | store_cost       | decimal(10,4) | NO   |     | NULL    |       |
# | units_sold       | decimal(10,4) | NO   |     | NULL    |       |
# | transaction_date | date          | YES  |     | NULL    |       |
# +------------------+---------------+------+-----+---------+-------+
#
Return a list of store name, year, month and total store_sales for each month that total store_sales increased from the previous month.
# */

with CTE as (
select
stores.name as store_name,
year(transaction_date) as `year`,
month(transaction_date) as `month`,
sum(store_sales) as total_sales
from
stores inner join sales
on stores.store_id = sales.store_id
group by stores.name , year(transaction_date) , month(transaction_date)
 )
 SELECT store_name,
        year,
        month,
        total_sales as curr_sales,
        lag(total_sales,1, 0) over(partition by store_name order by year || month ) as prev_sales
from CTE ;