# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]

        time: O(n), build hash map, buiding tree n times
        space: O(n), size for hash map, worst case for tree height is O(n)
        """

        # inorder: left - root - right
        # postorder: left - right - root
        # preorder: root - left - right
        # last element of porsorder is root
        inorder_map = {}
        for i, v in enumerate(inorder):
            inorder_map[v] = i

        self.idx = len(postorder) - 1

        def helper(left, right):
            if left > right:
                return None

            root_val = postorder[self.idx]
            self.idx -= 1

            root = TreeNode(root_val)

            mid = inorder_map[root_val]
            # build tree: root - right - left
            # build right first through preorder, right closer to root
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)





        