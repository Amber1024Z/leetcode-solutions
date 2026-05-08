# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        time: O(n)
        space: O(1)
        """
        if not head:
            return None

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break
        
        # no cycle: odd length -> fast.next = None, even length -> fast = None
        if not fast or not fast.next:
            return None

        # let slow start from head, fast start from meeting point, they will meet at the start of cycle
        # ex: [3,2,0,-4], pos = 1, they will meet at 4, then let slow start from head, fast start from -4, they will meet at 2 which is the start of cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast