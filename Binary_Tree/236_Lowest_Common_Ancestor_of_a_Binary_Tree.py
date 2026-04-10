# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        # use dict to store relationship Ex: parent[2] = 5, parent[5] = 3
        parent = {}
        parent[root] = None

        queue = deque()
        queue.append(root)

        # store dict until we have info about p and q
        while p not in parent or q not in parent:
            node = queue.popleft()
        
            if node.left:
                queue.append(node.left)
                parent[node.left] = node

            if node.right:
                queue.append(node.right)
                parent[node.right] = node

        # use set, search time will be O(1)
        ancestors = set()

        # add until root
        while p:
            ancestors.add(p)
            # ex: ancestor = (2, 5, 3)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q