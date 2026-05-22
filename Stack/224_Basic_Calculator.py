class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        
        time: O(n) where n is the length of the input string. We traverse the string once.
        space: O(n) in the worst case when we have nested parentheses
        """

        stack = []
        res = 0
        # 1 represents +, -1 represent -
        sign = 1
        i = 0
        n = len(s)

        while i < n:
            ch = s[i]

            if ch.isdigit():
                operand = 0

                while i < n and s[i].isdigit():
                    operand = operand * 10 + int(s[i])
                    i += 1
                
                # when we get complete num, combine sign store to res
                res += sign * operand
                continue

            elif ch == '+':
                sign = 1
            elif ch == '-':
                sign = -1

            elif ch == '(':
                # push prev num and sign into stack
                stack.append(res)
                stack.append(sign)
                # reset res and sign
                res = 0
                sign = 1
            elif ch == ')':
                prev_sign = stack.pop()
                prev_res = stack.pop()
                # 5 - (2 + 3) = 5+(−1)×5=0, that's why should sign * res
                res = prev_res + prev_sign * res

            i += 1

        return res