# WITH t(userid,view_count,view_date)
#          AS
#          (SELECT u.userid,v.view_count,v.view_date
#           FROM View v
#                    INNER JOIN User u
#                               ON u.userid=v.userid
#           WHERE u.user_type='user')
#
# SELECT a.userid,a.view_date,ROUND(AVG(b.view_count*1.0000),4) '3_day_running_avg'
# FROM t a
#          LEFT JOIN t b
#                    ON a.userid=b.userid
#                        AND b.view_Date BETWEEN a.view_date- INTERVAL '2 Days' AND a.view_Date


select
    Date,
    avg(view_count) over (order by view_date ROWS BETWEEN 2 PRECEDING and CURRENT ROW) as 3_day_running_avg
from views v
         join users u on v.user_id=u.id
where user_type ='user'