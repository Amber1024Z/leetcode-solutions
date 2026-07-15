# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool

        time: O(n), we have to check all nodes in the tree
        space: O(n) for unbalanced
        """
        
        # Bottom-up
        def helper(node):
            # each node will return if it's balanced, also height
            if not node:
                return True, -1

            # each node need report from left and right child
            leftBalance, leftHeight = helper(node.left)
            if not leftBalance:
                return False, 0

            rightBalance, rightHeight = helper(node.right)
            if not rightBalance:
                return False, 0

            # If the subtrees are balanced, check if the current tree is balanced
            # also return to parent's node height, remember + 1
            return (abs(rightHeight - leftHeight) < 2), 1 + max(leftHeight, rightHeight)
            
        return helper(root)[0]

            