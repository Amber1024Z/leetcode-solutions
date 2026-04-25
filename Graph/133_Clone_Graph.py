"""
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from xml.dom.minidom import Node


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node

        time: O(V + E), V is the number of nodes, E is the number of edges
        space: O(V), we need to keep size V of visited dictionary
        """
        if not node:
            return

        # key: original node, value: clone node, ex: visited = { node1: newNode1 }
        visited = {}

        def dfs(node):
            # if already visited, return its clone version
            if node in visited:
                return visited[node]

            clone = Node(node.val, [])
            visited[node] = clone

            for neighbor in node.neighbors:
                # call dfs find neighbor's clone
                neighbor_clone = dfs(neighbor)
                # add neighbor clone to curr clone's neighbors
                clone.neighbors.append(neighbor_clone)

            # return finished clone node
            return clone

        return dfs(node)

            
        