class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        
        time: O(n log n) because we need to sort the points by their end coordinate.
        space: O(1) 
        """

        if not points:
            return 0
        
        # sort by end point
        points.sort(key = lambda x:x[1])

        arrows = 1
        first_end = points[0][1]

        for i in range(1, len(points)):
            curr_start, curr_end = points[i]

            # if curr_start > last end, we need one more arrow
            if curr_start > first_end:
                arrows += 1
                first_end = curr_end

        return arrows


        