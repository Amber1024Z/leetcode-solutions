# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]

        time: O(n)
        space: O(1)
        """
        
        # we use 2 linked list, one smaller than x, another one >= x
        before_head = ListNode(0)
        before = before_head

        after_head = ListNode(0)
        after = after_head

        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next

        # avoid ring
        after.next = None

        before.next = after_head.next

        return before_head.next

