# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]

        time: O(H)
        space: O(n)
        """
        
        if not root:
            return None
        
        # search key whether if its exists
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # if we find key
        else:
            # if curr node don't have left or right
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # find max on left or min on right
            successor = root.left
            while successor.right:
                successor = successor.right
            
            # update new val for root
            root.val = successor.val

            # delete prev successor
            root.left = self.deleteNode(root.left, successor.val)

        return root