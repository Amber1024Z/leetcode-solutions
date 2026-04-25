class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        time: O(mn), m is the number of rows, n is the number of cols
        space: O(mn) in worst case, both the visited set and the DFS call stack can grow up to mn when the grid is filled with lands.
        """
        if not grid or not grid[0]:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def dfs(r, c):
            # stop case, out of range/water/visited
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols or grid[r][c] == '0' or (r, c) in visited:
                return 

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r - 1, c)

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '1'and (r, c) not in visited:
                    num_islands += 1
                    dfs(r, c)

        return num_islands
