class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int

        time: O(n)
        space: O(n)

        remain stack will store idx of unmatched left parentthess
        """
        stack = []
        # push -1 for edge case, ex: (), stack =[-1, 0], max_len = 1 - (-1) = 2
        stack.append(-1)
        max_len = 0

        # As long as the middle part is a valid match, they will all be popped
        # stack[-1] represents last invalid pos
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
        