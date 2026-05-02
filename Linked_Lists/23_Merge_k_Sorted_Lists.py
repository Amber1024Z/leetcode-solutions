# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        
        time: O(N log k) where N is the total number of nodes in all lists and k is the number of lists. K is the 
        number of lists because we are pushing and popping from the heap k times for each node.
        
        space: O(k) because we are storing at most k nodes in the heap at any time (one from each list).
        """
        min_heap = []

        for i, l in enumerate(lists):
            if l:
                # push first element for each list (node.val, idx, node)
                heapq.heappush(min_heap, (l.val, i, l))

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)

            # connect pop(smallest) node to curr.next
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next

        