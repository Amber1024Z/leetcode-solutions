class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool

        time: O(V + (E * a)), a is Inverse Ackermann Function, called E times for union 
        space: O(V)
        """

        uf = UnionFind(n)

        # connect all edges
        for edge in edges:
            uf.union(edge[0], edge[1])

        return uf.find(source) == uf.find(destination)
        