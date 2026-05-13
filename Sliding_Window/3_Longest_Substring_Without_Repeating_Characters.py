class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        time: O(n)
        space: O(1), since the char_set will at most have 26 characters, we can consider it as constant space
        """

        char_set = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            # if s[r] already in set, narrow down
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            # add s[r] to char_set
            char_set.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length
