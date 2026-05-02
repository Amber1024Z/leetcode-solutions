import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]

        time: O(klogk), iterate k times, each time push and pop from heap O(logk), total O(klogk)
        space: O(k) for heap, also O(k) for ans, total O(k)
        """
        m, n = len(nums1), len(nums2)
        ans = []
        visited = set()

        # (sum, (idx1, idx2))
        heap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))

        while k > 0 and heap:
            val, (i, j) = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))

            k = k - 1

        return ans


            
        