# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool

        time: O(n)
        space: O(1)
        """
        if not head or not head.next:
            return True

        def getMid(node):
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow.next
            slow.next = None

            return mid

        def reverse(node):
            prev = None
            curr = node

            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        second = getMid(head)
        reversed_head = reverse(second)

        # since left will have 1 more, compare until finish right
        head1, head2 = head, reversed_head
        while head2:
            if head1.val == head2.val:
                head1 = head1.next
                head2 = head2.next
            else:
                return False
        
        return True


        