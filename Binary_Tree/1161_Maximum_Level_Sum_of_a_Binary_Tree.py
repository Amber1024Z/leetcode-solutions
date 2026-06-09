from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int

        time: O(n)
        space: O(n)
        """
        if not root:
            return 

        queue = deque()
        queue.append(root)
        max_sum = float('-inf')
        max_level = 1
        curr_level = 0

        while queue:
            curr_len = len(queue)
            curr_sum = 0
            curr_level += 1

            for _ in range(curr_len):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # after process curr level, compare with max_sum
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = curr_level

        return max_level
    