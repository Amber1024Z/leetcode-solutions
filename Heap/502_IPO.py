import heapq
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int

        time: sort will be O(nlogn), iterate k times, each time push and pop from heap O(logn), total O(nlogn + klogn) => O(nlogn)
        space: O(n) for heap, also O(n) for projects, total O(n)
        """

        n = len(profits)
        projects = list(zip(capital, profits))
        # sort by capital, from low to high
        projects.sort()

        heap = []
        # ptr to check project idx, only look forward not backward
        # make sure check each project once, O(n)
        ptr = 0

        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                # use nagative to simulate max heap, push profit to heap
                heapq.heappush(heap, -projects[ptr][1])
                ptr += 1
            
            # if capital > w, no more projects we can do, stop
            if not heap:
                break

            # each time w will increase with profit
            # choose max profit project
            w += -heapq.heappop(heap)

        return w