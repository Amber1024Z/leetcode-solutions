class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        time: O(m * n)
        sapce: O(1) we do not need extra spcae, in-place fix 
        """
        m, n = len(grid), len(grid[0])

        # intialize first col
        for row in range(1, m):
            grid[row][0] = grid[row][0] + grid[row - 1][0]

        # initialize first row 
        for col in range(1, n):
            grid[0][col] = grid[0][col] + grid[0][col - 1]

        # update grid start at pos(1, 1)
        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row][col] + min(grid[row][col - 1], grid[row - 1][col])

        return grid[m - 1][n - 1]