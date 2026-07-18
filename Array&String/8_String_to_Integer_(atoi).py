class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int

        time: O(n)
        space: O(1)
        """
        
        # 1. skip all leading whitespace
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1 

        # all s is ' '
        if i == n:
            return 0

        # 2. check sign of '+' and '-'
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # 3. read consecutive number, if s[i] is not digit, then stop
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = num * sign

        # 4. rounding 
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN

        return num
