class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        
        time: O(nlogn)
        space: O(1)
        """
    
        intervals.sort()

        merged = []

        for interval in intervals:
            # if merged is empty or curr does not overlap with previous, append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # if overlap, merge curr and prev
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
                
