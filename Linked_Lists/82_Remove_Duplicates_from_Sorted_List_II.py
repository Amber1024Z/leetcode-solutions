# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        time: O(n)
        space: O(1)
        """
        # base case
        if not head or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        # prev is last distinct node
        prev, cur = dummy, head

        while cur:
            if cur.next and cur.val == cur.next.val:
                # if we find duplicate, keep skip until find distinct
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next

                # connect prev with next distict node
                prev.next = cur.next

            # if we did not find duplicate number, prev can move to next
            else:
                prev = cur

            cur = cur.next

        return dummy.next

        

                


        