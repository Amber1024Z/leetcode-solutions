class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        since starts with 4 or 9 use the subtractive form, we separately deal 4, 9, 40, 90, 400, 900
        
        time: O(1) because max will process 13 times(size of digits), no matter how large num is.
        space: O(1) because size of digits is fixed = 13
        """

        # use list of tuples, make sure calculate from largest num to smallest
        digits = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        # use greedy algorithms
        roman_digits = []

        for value, symbol in digits:
            if num == 0:
                break

            # use divmod return quotient, remainder
            # count = num // value
            # num = num % value
            count, num = divmod(num, value)

            roman_digits.append(symbol * count)
        
        return ''.join(roman_digits)
