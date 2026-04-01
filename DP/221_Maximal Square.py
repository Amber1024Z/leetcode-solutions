class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])

        # dp[i][j] The side length of the largest square that can be formed with (i, j) as its bottom-right corner
        dp = []
        for i in range(m):
            dp.append([0] * n)

        # intialize first row and col
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    ) + 1
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dp[i][j])
        return res * res