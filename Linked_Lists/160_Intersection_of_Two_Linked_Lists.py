# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        
        a = Length of the exclusive part of A
        b = Length of the exclusive part of B
        c = Length of the common part
        
        pA travels a + c + b, pB travels b + c + a, they will meet at the end of common part, which is the intersection 
        node. If there is no common part, they will meet at None.

        time: O(n)
        space: O(1)
        """

        pA = headA
        pB = headB

        while pA != pB:
            # when pA finish self's path, switch to pB
            if pA is None:
                pA = headB
            else:
                pA = pA.next

            if pB is None:
                pB = headA
            else:
                pB = pB.next

        return pA


        