class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        time: O(nlogn)
        space: O(1)
        """
        # sort base on end time
        # end earlier will left more space for rest
        intervals.sort(key = lambda x:x[1])
        n = len(intervals)
        ans = 0

        # intinal first end as boundary
        end = intervals[0][1]

        for i in range(1, n):
            # if curr interval overlap with end, delete curr
            if intervals[i][0] < end:
                ans += 1
            # if curr is not overlap with prev, update new end
            else:
                end = intervals[i][1]

        return ans



        