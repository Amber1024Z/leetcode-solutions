# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]

        Ensure that the distance between slow and fast is always exactly n. When fast reaches the finish line, slow must 
        be positioned immediately before the node that is the nth from the end.

        time: O(n)
        space: O(1)
        """

        # slow fast pointer, if fast reach end, slow n away from end
        # fast run n step ahead
        fast = head
        for i in range(n):
            fast = fast.next

        # if after run n step we finished all path, means we need delete head
        if fast is None:
            return head.next

        slow = head
        # example: 1->2->3->4->5, n = 2, after run n step, fast will end at 5, slow end ar 3, exactly before 4, which is the node we want to delete
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head

        
        

