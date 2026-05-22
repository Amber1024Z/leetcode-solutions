class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        
        time: O(n * m), n is number of strs, m is length of first str
        space: O(1)
        """

        # let first str be prefix at beginning, then keep shirinking
        ans = strs[0]

        for s in strs[1:]:
            while not s.startswith(ans):
                # if not match, prefix's end move left for 1 idx
                ans = ans[:-1]

                if not ans:
                    return ''

        return ans