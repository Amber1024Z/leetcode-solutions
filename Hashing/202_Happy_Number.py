class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool

        time: log(n), Each call to get_next runs once per digit of n, and a number n has log₁₀(n) digits. After the first 
        call, the number shrinks drastically and stays small, so the dominant cost is that first step — giving us O(log n) 
        overall. A number has k digits, approximately 10^k, so k is approximately log₁₀(n).

        space: O(log(n)), In the worst case, we could have log₁₀(n) different numbers in our seen set before we find a repeat.
        """

        # get_next function will calculate the sum of squares of digits of a number, for example
        # get_next(122) -> 1^2 + 2^2 + 2^2 = 9   
        def get_next(number):
            total = 0
            while number > 0:
                # Return both the quotient and the remainder, (a // b, a % b)
                # divmod(10, 3) -> (3, 1)
                number, digit = divmod(number, 10)
                total += digit ** 2
            return total

        seen = set()

        # if n is in seen, means we have a loop, return false, otherwise we add n to seen and calculate the next number until n is 1 or n is in seen.
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

        