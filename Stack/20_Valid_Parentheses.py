class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        time: O(n): traverse the given string one character at a time and push and pop operations on a stack take O(1) time.
        space: O(n) for worst case
        """

        # stack: first in last out
        stack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                # if stack is empty, but there exists right parentheses, False
                if not stack:
                    return False

                top = stack.pop()

                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False

        return len(stack) == 0
        