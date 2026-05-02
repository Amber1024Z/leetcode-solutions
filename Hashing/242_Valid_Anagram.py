from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        both string must be same only order of letter is different
        
        time: O(n), we process each character in both the strings exactly once to determine if the strings are anagrams.
        space: O(1) since the size of the ASCII character set is fixed, we only need to store 26 lowercase letters in dict, so the space complexity is O(1).
        """

        if len(s) != len(t):
            return False
        
        counter = defaultdict(int)

        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1

        for value in counter.values():
            if value != 0:
                return False
        
        return True