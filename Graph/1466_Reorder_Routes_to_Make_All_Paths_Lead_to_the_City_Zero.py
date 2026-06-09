from collections import defaultdict
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int

        adj:
        0: [(1, 1), (4, 0)] 
        1: [(0, 0), (3, 1)]
        2: [(3, 1)]
        3: [(1, 0), (2, 0)]
        4: [(0, 1), (5, 1)]
        5: [(4, 0)]

        time: O(n), tree has n - 1 edges, each edge constructs twice u->v, v->u, visited each node once.
        space: O(n), visited, size for adj is 2(n - 1), recursion depth worst is O(n)
        """
        adj = defaultdict(list)

        # 1 means u -> v cost 1, 0 means v -> u cost 0
        for u, v in connections:
            adj[u].append((v, 1))
            adj[v].append((u, 0))     

        ans = [0]
        visited = set([0])

        def dfs(node):

            for nei, cost in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    ans[0] += cost
                    dfs(nei)

        dfs(0)
        return ans[0]