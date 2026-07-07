class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        平方根 n 一定在 2 到 x/2 之间

        time: O(logn)
        space: O(1)
        """
        if x < 4:
            if x == 0:
                return 0
            else: # x = 1, 2, 3
                return 1

        l, r = 2, x // 2
        while l <= r:
            m = (l + r) // 2
            num = m * m

            if num == x:
                return m
            elif num < x:
                l = m + 1
            else:
                r = m - 1
        # stop when l > r, l will be first > x, so return r
        return r 
        
