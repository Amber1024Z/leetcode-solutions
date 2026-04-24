class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int

        time: O(m * n), where m and n are the lengths of the two input strings
        space: O(m * n)
        """
        m, n = len(text1), len(text2)

        dp = []
        for i in range(m + 1):
            dp.append((n + 1) * [0])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if the characters at the current position in both strings are the same, we can extend the longest common subsequence found so far by 1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # if the characters at the current position in both strings are different, we can either ignore the character in text1 or ignore the character in text2,
                # and take the maximum of the two cases
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]