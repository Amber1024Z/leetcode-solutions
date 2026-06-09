from collections import deque
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int

        time: o(n^2)
        space: O(n), set contains all cities, for queue, first cities connected to all other cities.
        """
        # n represents how many cities we need to check
        n = len(isConnected)
        seen = set()

        ans = 0

        for i in range(n):
            # each individual city also a provinces (all diagonals are 1)
            if i not in seen:
                ans += 1

                # initialize queue for city we never visited before
                queue = deque()
                queue.append(i)
                seen.add(i)

                while queue:
                    node = queue.popleft()
                    for j in range(n):
                        # if city are connected, belongs to same provinces, ans don't need +1
                        if isConnected[node][j] == 1 and j not in seen:
                            seen.add(j)
                            queue.append(j)

        return ans
        