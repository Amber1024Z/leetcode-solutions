# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        
        Time Complexity: O(N) - each node visited once
        Space Complexity: O(1)
        """
        if not root:
            return None

        curr = root

        while curr:
            dummy = Node(0)
            tail = dummy
            
            # inner loop, same level move parallel
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                # curr move to next node on same level
                curr = curr.next
            
            # dummy.next point to first node on next level
            # move to next level
            curr = dummy.next

        return root