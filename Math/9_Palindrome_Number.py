class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        time: Time complexity : O(logn), We divided the input by 10 for every iteration

        space: O(1)
        """
        # if last digit is 0 and x is not 0, or x is nagative return False
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            # x % 10: take out last digit of x
            # * 10 就是"把已有的数字往左移一位腾出空间"，+ x%10 就是"把新取到的位填进去"
            reverted = reverted * 10 + (x % 10)
            # // 10 等价砍掉最后一位个位数
            x = x // 10

        # when length is even, check x == revertedNumber
        # when len is odd, ex:1 2 3 2 1, ignore 3, 123 // 10 = 12, corresponding to 12 on left
        if x == reverted or x == reverted // 10:
            return True
        return False

        