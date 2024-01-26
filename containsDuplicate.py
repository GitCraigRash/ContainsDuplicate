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
