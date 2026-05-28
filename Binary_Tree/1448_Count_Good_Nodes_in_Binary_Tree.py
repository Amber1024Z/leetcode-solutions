# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int

        time: O(n)
        space: O(h), if it's balanced O(logn), otherwise O(n) for recursion
        """
        if not root:
            return 0

        def dfs(node, max_val):
            if not node:
                return 0

            ans = 0
            if node.val >= max_val:
                ans += 1

            max_val = max(max_val, node.val)
            
            left_count = dfs(node.left, max_val)
            right_count = dfs(node.right, max_val)

            return ans + left_count + right_count

        return dfs(root, root.val)

          