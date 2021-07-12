### Schema  —> org_id , customer_id (PK) , org_name, created_date
#### desired output - org_name , daily_count, rolling_5_day_count

select org.*,
       count(customer_id) OVER(created_date ORDER BY
           RANGE BETWEEN INTERVAL '5' DAY PRECEDING AND CURRENT_ROW) as rolling_5_day
from org
