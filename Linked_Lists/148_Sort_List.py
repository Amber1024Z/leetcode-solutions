class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        time: O(n log n), merge sort
        space: O(log n) for recursive stack space
        """
        if not head or not head.next:
            return head
        
        def getMid(node):
            # mid is the start of right half, slow is the end of left half
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return mid

        def merge(l1, l2):
            dummy = ListNode(0)
            head = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next

                else:
                    head.next = l2
                    l2 = l2.next

                head = head.next
            
            head.next = l1 if l1 else l2
            return dummy.next

        mid_node = getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid_node)

        return merge(left, right)

        

