class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]

        time: O(n)
        space: O(1)
        """
        
        n = len(intervals)
        i = 0
        res = []

        # case 1, no overlapping 
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # case 2, overlapping
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # case 3, after merge, add rest intervals into res
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

        