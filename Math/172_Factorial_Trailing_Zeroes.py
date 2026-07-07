class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int

        末尾的0 = 10的个数 = 2 * 5的对数, 只要有一个 5, 就一定能找到一个 2 凑成一对，产生一个 0

        time: O(logn) we divide n by each power of 5. 
        space: O(1)
        
        """
        count = 0

        while n > 0:
            # keep check 5, 25, 125....
            n = n // 5
            count += n

        return count
                