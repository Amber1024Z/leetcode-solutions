# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]

        time: O(n + m), where n and m are the lengths of list1 and list2, respectively. We process each node in both lists exactly once.
        space: O(1)
        """
        
        dummy = ListNode(0)
        curr = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        # if list1 or list 2 still have node, just add it
        if list1 is not None:
            curr.next = list1
        elif list2 is not None:
            curr.next = list2

        return dummy.next
