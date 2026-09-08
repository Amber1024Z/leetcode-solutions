class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        time: O(n ^ 2)
        space: O(n ^ 2)
        """
        
        n = len(nums)

        dp = []

        # dp[l][r] represents idx from nums
        for _ in range(n):
            dp.append([0] * n)

        # from i to i means only have 1 number to choose
        for i in range(n):
            dp[i][i] = nums[i]

        for diff in range(1, n):
            # right = left + diff, max right is n - 1, thus left <= n - 1 - diff. 
            for left in range(n - diff):
                right = left + diff
                # dp[left][right] represents net gain from curr player
                dp[left][right] = max(nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1])

        # dp[0][n - 1] represent begins of game, must be player 1
        return dp[0][n - 1] >= 0