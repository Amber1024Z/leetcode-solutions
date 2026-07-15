class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

        time: O(M⋅N), we perform N operations for each of the M digits of the second number
        space: O(M + N) for [::-1] and str_list
        """
        
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1) + len(num2)
        ans = [0] * n

        first = num1[::-1]
        second = num2[::-1]

        # place means units, tens, hundreds, etc.
        # place = 1 means has 1 tail 0, place = 2 means has 2 tail zero
        for place1, digit1 in enumerate(first):
            # For each digit in second_number multiply the digit by all digits in first_number.
    
            for place2, digit2 in enumerate(second):
                # num_zeros also is idx for which pos we're currently processing
                num_zeros = place1 + place2

                # num_zero = 0 place on unit, num_zero = 1 place on tens ...
                # take prev carry out redo calculation, and put number back
                carry = ans[num_zeros]

                col = int(digit1) * int(digit2) + carry

                ans[num_zeros] = col % 10

                ans[num_zeros + 1] += col // 10

        if ans[-1] == 0:
            ans.pop()

        final = reversed(ans)

        str_list = []

        for digit in final:
            str_list.append(str(digit))

        return ''.join(str_list)



