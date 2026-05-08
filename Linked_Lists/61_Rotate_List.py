# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        
        time: O(n)
        space: O(1)
        """

        # connect list as ring to decide where to break
        if not head or not head.next or k == 0:
            return head

        # calculate length find old tail
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1

        # connect to ring
        old_tail.next = head

        # find out new position for new tail
        # rotate k means walk head to tail n -(k%n) - 1
        #The penultimate element is n−1 (index). The second-to-last element is n−2.
        # The k+1th element from the end is naturally n−(k+1), which is n−k−1.
        new_tail = head
        for _ in range(n - (k % n) -1):
            new_tail = new_tail.next

        # re-assign new head, break the ring
        new_head = new_tail.next
        new_tail.next = None

        return new_head 
        