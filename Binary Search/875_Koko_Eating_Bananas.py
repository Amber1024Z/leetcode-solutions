class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int

        time: O(nlogm), n is len(piles), m is max(piles)
        space: O(1)
        """

        # l, r means the speed, slowest we have to each 1 banana per hr
        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2

            spent = 0
            for pile in piles:
                # same like math.ceil
                spent += (pile + m - 1) // m
            
            if spent <= h:
                # m could be ans, can't skip
                r = m
            else:
                l = m + 1
        
        return l
        