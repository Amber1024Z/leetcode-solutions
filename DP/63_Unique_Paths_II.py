class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int

        arrive curr cell = arrive from left + arrive from up

        time: O(m * n), where m and n are the number of rows and columns in the grid
        space: O(n), where n is the number of columns in the grid
        """
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [0] * n
        dp[0] = 1
        
        # process row by row
        for r in range(m):
            # for each row, check first cell, update dp[0]
            if obstacleGrid[r][0] == 1:
                dp[0] = 0
            # then process the rest of the cells in the row, update dp[c]
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    dp[c] = dp[c] + dp[c - 1]

        return dp[-1]