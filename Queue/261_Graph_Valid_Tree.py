from collections import deque
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool

        time: O(V + E)
        space: O(V + E)
        """
        # tree can't contains any cycle
        # if it's valid tree, edges must == n - 1
        if len(edges) != n - 1:
            return False

        """
        since it's undirected edge, if start from A and end at B has more than 1 path, means there's a cycle.
        
        start -> ... -> nei
        start -> ... curr -> nei
        
        if nei is alreay in visited, and this nei is not my parent, menas there must
        has a path from start to nei in previous, this will result a cycle.
        """

        adj = []

        for _ in range(n):
            adj.append([])

        # undirected edge, both are parents to each other
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        queue = deque()
        
        # queue will store node self also it's parents. 0 is start, assume parent is -1
        queue.append((0, -1))
        visited = set([0])

        while queue:
            node, parent = queue.popleft()

            for neigh in adj[node]:
                # case 1, neigh is my parent
                if neigh == parent:
                    continue
                
                # if neigh is not my parent, but already visited
                if neigh in visited:
                    return False
                
                visited.add(neigh)
                queue.append((neigh, node))

        return n == len(visited)




        
        