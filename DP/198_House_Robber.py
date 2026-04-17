class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n) we traverse the array once
        space: O(n) we use a dp array of size n to store the maximum amount
        """
        n = len(nums)
        dp = [0] * n 

        dp[0] = nums[0]
        # for the second house, we can only rob it or not rob it, we cannot rob the first house and the second house together since they are adjacent
        dp[1] = max(nums[0], nums[1])
        
        # for the rest of the houses, we have two options: either we rob the current house and add it to the maximum amount from two houses ago (dp[i - 2] + nums[i]), or we do not rob the current house and take the maximum amount from the previous house (dp[i - 1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]