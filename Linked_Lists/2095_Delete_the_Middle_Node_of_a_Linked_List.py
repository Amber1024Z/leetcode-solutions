# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        time: O(n)
        space: O(1)
        """
        if not head or not head.next:
            return None

        fast = head
        slow = head

        prev = None

        while fast and fast.next:
            # prev will stop 1-idx before the node need to be deleted
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        # when fast stop, slow will point to the node wo need to delete
        prev.next = slow.next
        return head