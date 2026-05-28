class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str

        time: O(n)
        space: O(n) for stack
        """

        stack = []

        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()

        return ''.join(stack)