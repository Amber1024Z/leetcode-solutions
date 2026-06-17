class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int

        time: O(n)
        sapce: O(1)
        """
        
        ans = 0

        while a or b or c:
            # check from right to left
            # 0 & 1 = 0, 1 & 1 = 1
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            # if last digit of c is 0, check if a and b last digit if it's 1
            if bit_c == 0:
                ans += bit_a + bit_b
            # if last digit of c is 1, a or b only need one of them be 1
            else:
                if bit_a == 0 and bit_b == 0:
                    ans += 1

            # after check last digit, get rid of last digit
            a >>= 1
            b >>= 1
            c >>= 1
        
        return ans