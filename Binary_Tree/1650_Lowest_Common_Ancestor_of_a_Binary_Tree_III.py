"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node

        time: O(n)
        space: O(1)
        """
        # calculate depth for p and q
        def depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.parent
            return depth

        depth_p = depth(p)
        depth_q = depth(q)

        # let deeper node climb up until height is equal
        while depth_p > depth_q:
            p = p.parent
            depth_p -= 1

        while depth_p < depth_q:
            q = q.parent
            depth_q -= 1

        # when p q on same level, climb up together until reach
        while p != q:
            p = p.parent
            q = q.parent

        return p