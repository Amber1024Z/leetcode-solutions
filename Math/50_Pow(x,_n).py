class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        n is even: x^n = (x^2)^(n/2)
        n is odd: x^n = x * (x^2)^((n - 1)/2),提前乘以一个n, n - 1让n变成偶数
        
        time: O(logn), we divide n by 2 for every iteration
        space: O(1)
        """
        if n == 0:
            return 1

        # if n < 0, x^-n = (1/x)^n
        if n < 0:
            n = -1 * n
            x = 1 / x
        
        res = 1.0
        while n > 0:
            # check whether n is odd
            if n % 2 == 1:
                res = res * x
                n -= 1
            x = x * x
            n = n // 2

        return res