import heapq
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int

        time: O(nlogn), for sorting takes nlogn, for each num push into heap at most once, which
        will takes nlognk. overall is nlogn if n > k

        space: O(N), size for heap is k, but size for pairs if n.
        """

        # pairs num from nums1 and nums2 with order, sorted base nums2 from large to small
        pairs = sorted(zip(nums2, nums1), reverse = True)

        heap = []
        curr_sum = 0
        ans = 0

        for n2, n1 in pairs:
            if len(heap) < k:
                heapq.heappush(heap, n1)
                curr_sum += n1
                # if size of heap == k, update first valid ans
                if len(heap) == k:
                    ans = curr_sum * n2
            else:
                # only when new n1 > heap[0], we update curr_sum and push to heap
                if n1 > heap[0]:
                    removed = heapq.heappop(heap)
                    curr_sum -= removed

                    # add new n1 to heap and calculate new curr_sum
                    heapq.heappush(heap, n1)
                    curr_sum += n1

                    # update new ans
                    ans = max(ans, curr_sum * n2)
                # if new n1 < heap[0], don't need to update
                else:
                    pass
        
        return ans

        

        
        