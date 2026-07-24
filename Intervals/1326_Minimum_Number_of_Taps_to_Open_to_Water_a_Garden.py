class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int

        time: O(nlogn) for sort
        space: O(n) for cover_range and sort
        """
        
        cover_range = []

        for i in range(n + 1):
            # valid range between [0, n]
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])
            cover_range.append([start, end])

        # sort base on start
        cover_range.sort()

        ans = 0
        curr_end = 0
        i = 0
        curr_far = 0
        m = len(ranges)

        while curr_end < n:
            # during first searching, need find start begins from 0 also with furthest end
            while i < m and cover_range[i][0] <= curr_end:
                curr_far = max(cover_range[i][1], curr_far)
                i += 1
            
            # if start from 0, we've already sort range, first range start > 0, means there's gap
            # in range  start <= curr_end, we can't extend to right
            if curr_far == curr_end:
                return -1

            curr_end = curr_far
            ans += 1

        return ans