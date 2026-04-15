from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node

        time: O(n), visit each node once
        space: O(n), queue size at most n/2 for last level
        """

        if not root:
            return None

        q = deque()
        q.append(root)

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                # if i == size -1, means cur node is last node at this level
                if i < size - 1:
                    node.next = q[0]
                else:
                    node.next = None 

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root

        
        