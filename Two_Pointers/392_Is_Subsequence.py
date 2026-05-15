class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        time: O(n)
        space: O(1)
        """

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            # if it's not match, only move j
            else:
                j += 1

        return i == len(s)
        