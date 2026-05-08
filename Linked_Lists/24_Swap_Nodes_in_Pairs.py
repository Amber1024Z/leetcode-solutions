# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        time: O(n)
        space: O(1)
        """

        if not head:
            return None
        dummy = ListNode(0)
        curr = dummy

        slow = head
        fast = head.next

        while fast:
            # store next round 'slow' and fast
            next_slow = fast.next
            if fast.next:
                next_fast = fast.next.next
            else:
                next_fast = None

            curr.next = fast
            fast.next = slow
            
            curr = slow
            slow = next_slow
            fast = next_fast

        # if length is odd, move curr to last slow node
        curr.next = slow

        return dummy.next
        
            
        
        