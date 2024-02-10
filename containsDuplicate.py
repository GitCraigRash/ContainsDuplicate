class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False

sql_statement = "SELECT customer_id FROM Customer Group by customer_id having COUNT(DISTINCT product_key) = (SELECT COUNT(product_key) FROM Product)"

import pandas as pd
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    pivots the data so that each row represents temperatures for a specific month, and each city is a separate column.
    """
    pivot_table = pd.pivot_table(weather,index='month', columns='city',values='temperature', aggfunc='sum')
    return pivot_table


sql_statement = "SELECT user_id, COUNT(follower_id) as followers_count FROM Followers Group by user_id ORDER by user_id ASC;"

sql_statement = "SELECT class FROM (SELECT COUNT(student) as student, class FROM Courses group by class) as a WHERE student >= 5"

sql_statement = "# Write your MySQL query statement below
SELECT person_name FROM (SELECT person_id, turn, person_name, @cumulative_sum:= @cumulative_sum + weight as cumulative_sum
FROM Queue
CROSS JOIN (SELECT @cumulative_sum := 0 ) AS init
Order By turn) as b1
WHERE cumulative_sum <= 1000
Order by turn desc
LIMIT 1
 "
sql_statement = "SELECT a1.activity_date as day, COUNT(DISTINCT a1.user_id) as active_users
FROM ( SELECT * FROM Activity) as a1
WHERE a1.activity_date < DATe_ADD("2019-06-27", INTERVAL 30 DAY) and a1.activity_date > "2019-06-27"
GROUP BY a1.activity_date 
"
sql_statement = "SELECT c.customer_id
FROM Customer c
Group by c.customer_id
having COUNT(DISTINCT c.product_key) >= (SELECT COUNT(*) as product_key FROM Product)
"

sql_statement = "SELECT ROUND((avg(if(d2.order_date = d2.customer_pref_delivery_date,1,0))*100),2) as immediate_percentage
FROM (SELECT customer_id,
MIN(order_date) as order_date,
MIN(customer_pref_delivery_date) as customer_pref_delivery_date
FROM Delivery
group by customer_id) as d2
"
sql_statement = "SELECT DATE_FORMAT(t1.trans_date, '%Y-%m') AS month,
t1.country,
COUNT(t1.state) as trans_count,
SUM(t1.state = "approved") as approved_count,
SUM(t1.amount) as trans_total_amount,
SUM(IFNULL(t2.amount,0)) as approved_total_amount
FROM Transactions t1
LEFT JOIN (SELECT id, amount FROM Transactions WHERE state = "approved") as t2
ON t1.id = t2.id
Group by MONTH(trans_date),YEAR(trans_date), country
"
sql_statement = "SELECT s.user_id, ROUND(avg(CASE WHEN action = "timeout" THEN 0
WHEN action = "confirmed" THEN 1 else 0 END),2) as confirmation_rate
FROM Signups s
Left Join Confirmations c
ON s.user_id = c.user_id
group by s.user_id
"
