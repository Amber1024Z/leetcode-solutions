# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool

        time: O(M + N)
        space: O(M + N) leafs + stack
        """
        def getLeaf(root, leafs):
            if not root:
                return

            if not root.left and not root.right:
                leafs.append(root.val)
                return

            getLeaf(root.left, leafs)
            getLeaf(root.right, leafs)
        
        leafs1 = []
        leafs2 = []

        getLeaf(root1, leafs1)
        getLeaf(root2, leafs2)

        return leafs1 == leafs2