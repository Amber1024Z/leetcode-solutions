class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        time: O(1), A standard 32-bit signed integer has at most 10 decimal digits
        space: O(1)
        """
        sign = 1

        if x == 0:
            return 0
        elif x < 0:
            sign = -1

        x = abs(x)

        res = 0

        while x > 0:
            curr = x % 10
            res = res * 10 + curr
            x = x // 10
        
        if sign == -1:
            res = -res

        if (res > 2** 31) or (res < -2 ** 31):
            return 0
        else:
            return res


        
