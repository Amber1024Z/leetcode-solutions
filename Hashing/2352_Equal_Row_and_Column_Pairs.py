from collections import Counter
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        time: O(n^2), check each element in grid
        space: O(n^2) for Counter.
        """

        n = len(grid)

        row_count = Counter()

        for r in range(n):
            # convert row into tuple for hash
            row = tuple(grid[r])
            row_count[row] += 1

        ans = 0

        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            col = tuple(col)
            # check curr col if it's exsit in row_counter
            ans += row_count[col]
        
        return ans