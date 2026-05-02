from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        time: O(nlogk), we need to push or pop n numbers, each push or pop operation will take logk time, since we maintain size k heap.
        space: O(k), we maintain size k heap.
        """

        freq = Counter(nums)
        heap = []

        for num, fre in freq.items():
            heapq.heappush(heap, (fre, num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for fre, num in heap:
            res.append(num)

        return res