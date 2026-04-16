# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int

        time: O(n)
        sapce: O(H), h is height of tree
        """
        if not root:
            return 0

        ans = 0
        stack = [(root, 0)]

        while stack:
            root, curr_num = stack.pop()
            curr_num = curr_num * 10 + root.val

            # check if we reach leaf
            if not root.left and not root.right:
                ans += curr_num

            if root.left:
                stack.append((root.left, curr_num))
            if root.right:
                stack.append((root.right, curr_num))

        return ans



