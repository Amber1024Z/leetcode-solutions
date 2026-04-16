# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int

        algorithm that runs in less than O(n) time complexity.

        time: O(log(n) * log(n)) calculate height is O(log(n)), and we do it for each level of tree O(log(n))
        space: O(log(n)) since it's a complete tree, the height is O(log(n))
        """
        
        if not root:
            return 0

        def calculate_left(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def calculate_right(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        left_height = calculate_left(root)
        right_height = calculate_right(root)

        # if left == right, it's a perfect subtree: 2^h - 1 nodes
        if left_height == right_height:
            return 2 ** left_height - 1

        # otherwise recursively count
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
                

        
        