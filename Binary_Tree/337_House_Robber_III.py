# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int

        time: O(n), unbalanced tree
        space: O(n)
        """

        # key concept is compare max value between rob this node or NOT rob this node
        def helper(node):
            if not node:
                # return [rob this node, not rob this node]
                return (0, 0)

            left = helper(node.left)
            right = helper(node.right)

            # if we decide rob curr node, then we can't rob it's children
            rob = node.val + left[1] + right[1]
            # if we do not rob curr node, we take max val from left and right
            not_rob = max(left) + max(right)

            # return res to parent node
            return (rob, not_rob)

        return max(helper(root))