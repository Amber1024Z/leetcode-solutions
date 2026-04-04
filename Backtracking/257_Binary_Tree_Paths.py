# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]

        time: for balance tree, each path avg length is logn, we have n nodes, so overall is O(nlogn)
        space: O(n)
        """

        if not root:
            return []
        
        res = []

        def construct_path(node, path):
            if node:
                path += str(node.val)

                if not node.left and not node.right:
                    res.append(path)
                else:
                    path += '->'
                    construct_path(node.left, path)
                    construct_path(node.right, path)

        construct_path(root, '')

        return res


            