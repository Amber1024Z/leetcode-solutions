class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int

        time: O(1), 32-bit integer
        space: O(1)
        """

        ans = 0
        while n:
            # last digit & 1, if ans is 1, ans += 1
            if n & 1 == 1:
                ans += 1
            # get gid of last digit
            n = n >> 1

        return ans
      

        