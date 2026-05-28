# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        time: O(n)
        space: O(1)
        """

        if not head or not head.next:
            return head

        odd = head
        # we don't care about val in node, only focus on idx
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        # connect odd with evenhead
        odd.next = even_head

        return head