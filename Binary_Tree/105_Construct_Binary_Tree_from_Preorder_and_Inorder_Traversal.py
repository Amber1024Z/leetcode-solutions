# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]

        preorder = [3, 9, 20, 15, 7]
        inorder  = [9, 3, 15, 20, 7]
        inorder_map = {9:0, 3:1, 15:2, 20:3, 7:4}
        pre_idx = 0

        time: O(n), build hash map, buiding tree n times
        space: O(n), size for hash map, worst case for tree height is O(n)
        """

        # preorder: Root - Left - Right
        # inorder: left - root - right
        # first node in preorder must be root, use this divide L and R in inorder
        inorder_map = {}
        for i, v in enumerate(inorder):
            inorder_map[v] = i

        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # find out cut point for L and R
            mid = inorder_map[root_val]
            # construct left tree
            root.left = helper(left, mid - 1)
            # construct right tree
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)



        