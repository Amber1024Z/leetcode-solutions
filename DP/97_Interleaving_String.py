class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool

        time: O(n1 * n2), where n1 and n2 are the lengths of s1 and s2
        space: O(n1 * n2)
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        dp = []
        # ex: a,b,c need 4 rows, because we need to consider the case of empty string, take 0 to take all 4 chars
        for _ in range(n1 + 1):
            dp.append([False] * (n2 + 1))

        # most left cornner
        dp[0][0] = True

        # intialize first col(only use s1)
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        # initialize first row(onlu use s2)
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
            # check can match from top or from left, if can match from top
                from_top = dp[i-1][j] and s1[i - 1] == s3[i + j -1]
                from_left = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = from_top or from_left

        return dp[n1][n2]