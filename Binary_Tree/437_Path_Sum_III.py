# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int

        time: O(n)
        space: O(n)
        """
        self.count = 0
        h = defaultdict(int)

        def preorder(node, curr_sum):

            if not node:
                return 

            curr_sum += node.val
            if curr_sum == targetSum:
                self.count += 1

            self.count += h[curr_sum - targetSum]
            h[curr_sum] += 1

            # process left
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
 
            # Remove the current sum from the hashmap
            # ex: we are preocess node 10, after that, back to 10's parent 5, we need remove 10's info from dict
            h[curr_sum] -= 1

        preorder(root, 0)
        return self.count
