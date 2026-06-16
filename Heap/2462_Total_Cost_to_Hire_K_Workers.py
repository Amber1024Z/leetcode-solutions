import heapq
from heapq import heapreplace
class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int

        time: O(m + (k * logm)), in python, heapify takes linear time of O(m), m = cadidates,
        we need process k times for push and pop from heap, thus it's k * logm

        space: O(m) size for both queues.
        """

        # edge case, at beginning left and right has overlap, thus we don't need 2 heaps
        n = len(costs)
        ans = 0

        if n <= 2 * candidates:
            heapq.heapify(costs)
            ans = 0
            for _ in range(k):
                ans += heapq.heappop(costs)
            return ans

        # we need 2 heaps
        left_h = costs[:candidates]
        right_h = costs[-candidates:]

        heapq.heapify(left_h)
        heapq.heapify(right_h)
        
        # l and r point to next candiate for left heap and right heap
        l = candidates 
        r = n - candidates - 1

        for _ in range(k):
            if left_h:
                n1 = left_h[0]
            else:
                n1 = float('inf')
            
            if right_h:
                n2 = right_h[0]
            else:
                n2 = float('inf')

            # left heap has priority, Break the tie by the smallest index.
            if n1 <= n2:
                # if middle part has candidates, pop from left and add costs[l] to left
                if l <= r:
                    # heapreplace will return the pop out num and push costs[l]
                    ans += heapreplace(left_h, costs[l])
                    l += 1
                # if no number in middle, just pop out the num
                else:
                    ans += heapq.heappop(left_h)
            else:
                if l <= r:
                    ans += heapreplace(right_h, costs[r])
                    r -= 1
                else:
                    ans += heapq.heappop(right_h)

        return ans 




        