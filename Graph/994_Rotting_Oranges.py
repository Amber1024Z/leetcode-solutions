from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        time: O(mn), m is the number of rows, n is the number of cols, we need to traverse the whole grid once to 
        initialize the queue and visited set

        space: O(mn) when the grid is filled with rotten and fresh oranges, all cells may be added to the queue and visited set.
        """

        num_rows, num_cols = len(grid), len(grid[0])
        visited = set()
        ans, fresh = 0, 0
        queue = deque()

        for r in range(num_rows):
            for c in range(num_cols):
                # put all rotten oranges into queue
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while queue and fresh > 0:
            ans += 1

            for _ in range(len(queue)):
                curr_r, curr_c = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = curr_r + dr, curr_c + dc

                    if 0 <= nr < num_rows and 0 <= nc < num_cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        fresh -= 1
                        queue.append((nr, nc))

        if fresh == 0:
            return ans
        else:
            return -1

                 
