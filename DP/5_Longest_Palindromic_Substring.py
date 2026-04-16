class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        Expand From Centers, try both odd/even center expanding.

        time: O(n^2) worst case when every character in the string is the same.
        space: O(1)
        """
        res = ''
        resLen = len(res)

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1
        
        return res
