# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool

        time: O(n), each node visited once check if it's valid
        space: O(n), worst case tree's height is O(n)
        """

        # low, high is boundary for curr node
        def helper(node, low, high):
            # empty node is BST
            if not node:
                return True

            if not (low < node.val < high):
                return False

            # left must smaller than curr node, right must greater then curr node
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root, float('-inf'), float('inf'))

