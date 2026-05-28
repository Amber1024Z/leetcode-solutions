# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int

        time: O(n)
        space: O(1)
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow will point to first element on right half
        def reverse(node):
            prev = None
            curr = node

            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        # reverse right half
        p2 = reverse(slow)
        p1 = head

        ans = -float('inf')
        while p2:
            curr_sum = p1.val + p2.val
            ans = max(ans, curr_sum)

            p1 = p1.next
            p2 = p2.next

        return ans