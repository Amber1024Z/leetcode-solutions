class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        dp[i-1][j-1]  ← Top-left: replacement operation
        dp[i-1][j]    ← Top: deletion operation
        dp[i][j-1]    ← Left: insertion operation

        time: O(m*n)
        space: O(m*n)
        """
        len1, len2 = len(word1), len(word2)
        if len1 == 0:
            return len2
        if len2 == 0:
            return len1
        
        dp = []
        for _ in range(len1 + 1):
            dp.append([0] * (len2 + 1))

        # base case, initialize first row and col
        for i in range(1, len1 + 1):
            dp[i][0] = i
        for j in range(1, len2 + 1):
            dp[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # if same, check diagonal
                if word2[j - 1] == word1[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # if not same, check top, left and diagonal and add 1 for current operation
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    ) + 1

        return dp[len1][len2]