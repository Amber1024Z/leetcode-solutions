# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        1 → 2 → 3 → None
        None ← 1 ← 2 ← 3

        time: O(n)
        space: O(1)
        """
        prev = None
        curr = head

        while curr:
            # store next node
            next_temp = curr.next
            # reverse curr direction
            curr.next = prev
            # move prev
            prev = curr
            # move curr
            curr = next_temp

        # at the end, curr point to 3, next_temp point to 3.next is None, prev point to 3, thus return prev
        return prev
