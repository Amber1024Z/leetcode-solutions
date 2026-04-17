class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        time: O(m*n)
        space: O(m*n)
        """
        dp = []
        for i in range(m):
            dp.append([0] * n)

        dp[0][0] = 0

        # valid path must from top and left
        # initialize first row
        for c in range(n):
            dp[0][c] = 1
        # initialize first col
        for r in range(m):
            dp[r][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]