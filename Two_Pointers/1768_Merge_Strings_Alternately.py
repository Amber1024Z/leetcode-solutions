class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str

        time: O(m + n)
        space: O(1)
        """
        
        i, j = 0, 0
        ans = ''

        while i < len(word1) and j < len(word2):
            ans += word1[i]
            i += 1

            ans += word2[j]
            j += 1

        if i < len(word1):
            ans += word1[i:]
        else:
            ans += word2[j:]

        return ans