from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int

        time: O(m * n)
        space: O(m * n) for visited and queue
        """

        rows, cols = len(maze), len(maze[0])
        # r, c, steps
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            r, c, steps = queue.popleft()
            for dr, dc in ([1,0],[0,1],[-1,0],[0,-1]):
                new_r, new_c = r + dr, c + dc
                # check boundaris
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if maze[new_r][new_c] == '+':
                    continue
                if (new_r, new_c) in visited:
                    continue
                if new_r == 0 or new_r == rows - 1 or new_c == 0 or new_c == cols - 1:
                    return steps + 1
                
                visited.add((new_r, new_c))
                queue.append((new_r, new_c, steps + 1))
        
        return -1