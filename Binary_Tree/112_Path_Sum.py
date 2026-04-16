# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool

        time: O(n) visit each node exactly once
        space: O(n) tree is completely unbalanced
        """

        if not root:
            return False

        # use dfs, stack store curr node and curr_sum
        stack = [(root, targetSum - root.val)]

        while stack:
            node, curr_sum = stack.pop()

            # check if we reach leaf
            if not node.left and not node.right  and curr_sum == 0:
                return True

            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))

        return False
        


