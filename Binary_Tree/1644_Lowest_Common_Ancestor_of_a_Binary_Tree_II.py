# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        Diff: p and q may not exists, need to check tree contains p and q firstly.

        time/space: O(n)
        """

        self.p_found = False
        self.q_found = False

        # search p and q if exits
        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p:
                self.p_found = True
                return node
            if node == q:
                self.q_found = True
                return node
            
            if left and right:
                return node

            return left if left else right

        res = dfs(root)

        if self.p_found and self.q_found:
            return res
        return None