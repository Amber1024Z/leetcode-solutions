# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int

        time: O(n)
        space: O(n) for unbalanced tree (list), otherwise it's O(logn)
        """
        self.length = 0

        # goLeft -> boolean, steps is curr zigzag path has how many steps
        def dfs(node, goLeft, steps):
            if not node:
                return
                
            # when node exsits, update length immediatly
            self.length = max(self.length, steps)

            if goLeft:
                # follow path, step + 1
                dfs(node.left, False, steps + 1)
                # if not follow pattern, we try diff path, steps will reset to 1
                dfs(node.right, True, 1)
            else:
                # follow path, steps + 1
                dfs(node.right, True, steps + 1)
                # not follow, reset steps to 1
                dfs(node.left, False, 1)
        
        dfs(root, True, 0)
        return self.length


        