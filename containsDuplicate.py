class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False

SELECT user_id, COUNT(follower_id) as followers_count FROM Followers
Group by user_id
ORDER by user_id ASC;
