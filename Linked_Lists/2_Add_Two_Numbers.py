# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]

        time: O(max(m,n))
        space: O(1)
        """
        
        dummyHead = ListNode(0)
        curr = dummyHead
        # 5+7 = 12, carry will 1
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None:
                l1_val = l1.val
            else:
                l1_val = 0

            if l2 is not None:
                l2_val = l2.val
            else:
                l2_val = 0

            # calculate the sum of curr col
            colSum = l1_val + l2_val + carry

            # if sum is 13, carry is 1: 13//10 = 1
            carry = colSum // 10

            # if sum is 13, curr node is 13 % 10 = 3
            digit = colSum % 10

            # creat a new node after curr
            newNode = ListNode(digit)
            curr.next = newNode
            curr = newNode

            # both node move to next position
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummyHead.next