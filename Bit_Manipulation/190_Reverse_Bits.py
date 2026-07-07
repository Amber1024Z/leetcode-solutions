class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int

        time: O(1), the number of iteration is fixed regardless the input, since the integer is of fixed-size (32-bits) in our problem.

        space: O(1), since the consumption of memory is constant regardless the input.
        """
        
        ans, power = 0, 31
        
        # i = 31 - i, i = 0 - > 31, i = 1 -> 30

        while n:
            # << 31, << 30 ....
            ans += (n & 1) << power
            n = n >> 1
            power -= 1

        return ans

