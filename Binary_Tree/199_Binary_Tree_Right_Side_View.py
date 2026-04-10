# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]

        time: O(n)
        space: O(n)
        """

        if not root:
            return []

        queue = deque()
        queue.append(root)

        ans = []

        while queue:
            curr_length = len(queue)

            for i in range(curr_length):
                node = queue.popleft()

                if i == curr_length - 1:
                    ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans
    