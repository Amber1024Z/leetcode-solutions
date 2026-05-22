class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        time: O(n)
        space: O(1)
        """

        res, idx = 0, len(s) - 1

        while idx >= 0:
            if s[idx] != ' ':
                res += 1

            elif res > 0:
                return res

            idx -= 1


        return res