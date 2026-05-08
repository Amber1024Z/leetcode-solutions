# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        
        time: O(n)
        space: O(1)
        """

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # EX 1,2,3,4,5, we wanna reverse 2, 3, 4
        # leftprev point at 1, cur point 2, iterate left - 1 times
        leftprev, cur = dummy, head
        for _ in range(left - 1):
            leftprev, cur = cur, cur.next
        
        # now cur = left, leftprev is node before left
        prev = None
        for i in range(right - left + 1):
            temNext = cur.next
            cur.next = prev
            prev, cur = cur, temNext

        # cur is point to 5, node after right
        # leftprev.next is still 2, so next.next need connect with 5
        leftprev.next.next = cur
        # prev is point to 4
        leftprev.next = prev

        return dummy.next

        