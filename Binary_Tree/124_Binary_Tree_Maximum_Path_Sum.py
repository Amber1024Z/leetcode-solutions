# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int

        for valid path can not pass same node twice 
        for any node has 2 options: bridge or arm 

        time: O(n) each node visited only once
        space: O(n) worst case tree is a linked list, so the height is n.

        """
        self.max_path = float('-inf')

        def findPath(node):

            if not node:
                return 0

            # if left/right provide nagative val, we give up, even 1 node itself can be a path
            left_path = max(findPath(node.left), 0)
            right_path = max(findPath(node.right), 0)

            # use curr node as bridge to calculate max_path
            self.max_path = max(self.max_path, node.val + left_path + right_path)
            
            # use curr node as arm, report to patent node, only choose 1 path form left or right
            return max(left_path + node.val, right_path + node.val)

        findPath(root)
        return self.max_path