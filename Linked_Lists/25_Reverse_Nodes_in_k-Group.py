# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        
        time: O(n), where n is the number of nodes in the linked list. We traverse the linked list once to reverse the nodes in groups of k.
        space: O(1), since we are reversing the nodes in place and not using any additional data structures that grow with the input size.
        """

        # helper func to reverse each small group
        def reverseLinkedList(head, k):
            curr = head
            prev = None

            while k:
                next_temp = curr.next 
                curr.next = prev
                prev = curr
                curr = next_temp
                k -= 1

            # return new head for curr reversed group
            return prev
        
        # ptr to recored which node we are at 
        ptr = head
        # recored tail for curr reversed group, we will connect it with next reversed group
        ktail = None
        # only fix once at begining
        new_head = None

        while ptr:
            count = 0
            # recored start for each group
            group_head = ptr

            # iterate until length reach k
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            if count == k:
                curr_new_head = reverseLinkedList(group_head, k)
                # at begining we don't have new head, set it to curr_new_head
                if not new_head:
                    new_head = curr_new_head
                # if we have ktail, connect it with curr_new_head
                if ktail:
                    ktail.next = curr_new_head
                
                # update ktail each round to connect with next reversed group
                ktail = group_head

            # if rest length < k, connect rest to ktail
            else:
                ktail.next = group_head

        if new_head:
            return new_head
        else:
            return head

