import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        time: O(nlogk), we need to push or pop n numbers, each push or pop operation will take logk time, since we maintain size k heap.
        space: O(k), we maintain size k heap.
        """
        # we maintain size k min heap, heap[0] will be kth largest nuumber
        heap = []

        for num in nums:
            # min heap, push or pop (logn)
            heapq.heappush(heap, num)

            # we maintain size k heap
            if len(heap) > k:
                # popout smallest element
                heapq.heappop(heap)

        # at and, we will have size k heap, return first element will be Kth
        return heap[0]