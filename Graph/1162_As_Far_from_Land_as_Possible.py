from collections import deque


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        0: water 1: island 
        use BFS, 1 layer == 1 distance

        time: O(mn), m is the number of rows, n is the number of cols, we need to traverse the whole grid once to 
        initialize the queue and visited set

        space: O(mn) all cells are added to the visited set and queue
        """
        queue = deque()
        max_distance = -1
        distance = 0
        visited = set()

        num_rows, num_cols = len(grid), len(grid[0])

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    visited.add((row, col))
        
        if len(queue) == 0 or len(queue) == num_rows * num_cols:
            return -1

        while queue:
            distance += 1

            for _ in range(len(queue)):
                curr_r, curr_c = queue.popleft()

                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if (0 <= nr < num_rows and 0 <= nc < num_cols 
                    and grid[nr][nc] == 0 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        max_distance = max(distance, max_distance)
                        queue.append((nr, nc))

        return max_distance



        