from collections import deque

class Solution(object):
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        time: O(V + E), V is the number of courses, E is the number of prerequisites
        space: O(V + E), we need to keep the graph and the indegree array
        """
        indegree = numCourses * [0]
        adj = []
        for _ in range(numCourses):
            adj.append([])

        # 1. create graph for dependend relationship
        for prerequisite in prerequisites:
            # since need to take [1] first
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        # 2. initialize queue
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        nodeVisited = 0

        # 3. BFS
        while queue:
            node = queue.popleft()
            nodeVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return numCourses == nodeVisited


        