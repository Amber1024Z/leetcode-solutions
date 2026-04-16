# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        # since it's binary search tree, leftmost node is the smallest, we can use stack to store path to leftmost node
        self.stack = []
        self._leftmost_inorder(root)

    # stack will append node until we reach leftmost node, so top of stack is the smallest node
    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int

        time: O(1) amortized, each node is visited at most twice, once when it's added to stack and once when it's removed from stack
        space: O(h), h is height of tree, worst case O(n)
        """
        # top of stack is the smallest node
        topmost_node = self.stack.pop()

        # we add all leftmost nodes of right child to stack
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)

        return topmost_node.val
    
    def hasNext(self):
        """
        :rtype: bool

        time: O(1)
        space: O(1)
        """
        return len(self.stack) > 0