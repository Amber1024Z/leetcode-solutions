class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        time: O(V + E), V is the number of courses, E is the number of prerequisites
        space: O(V + E), we need to keep the graph and the indegree array
        """
        # graph
        adj = []
        for _ in range(numCourses):
            adj.append([])

        indegree = [0] * numCourses

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        # queue
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        visitedNode = 0
        result = []
        # bfs
        while queue:
            node = queue.popleft()
            visitedNode += 1
            result.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if visitedNode == numCourses:
            return result
        else:
            return []



        