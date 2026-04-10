# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.

        time: O(n)
        space: O(1)
        """
        # preorder: root-l-r, left tree must before right
        if not root:
            return None

        node = root
        while node:
            if node.left:
                # find right most node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                # let left tree connect with right tree
                rightmost.right = node.right
                node.right = node.left
                node.left = None

            node = node.right
