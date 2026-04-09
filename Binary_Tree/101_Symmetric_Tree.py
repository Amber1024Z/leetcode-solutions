# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool

        time/space: O(n)
        """

        if not root:
            return True

        def helper(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return helper(p.left, q.right) and helper(p.right, q.left)

        return helper(root, root)