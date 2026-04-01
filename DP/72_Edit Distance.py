class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        替换: word1[i] 换成 word2[j]，两个都匹配消耗掉
        → i-1, j-1

        删除:word1[i] 删掉,word2不动
            → word1少一个,i-1
            → word2没消耗,j不变

        插入:插入word2[j]到word1,word2[j]匹配消耗掉
            → word1没动,i不变
            → word2少一个,j-1

        递归从末尾往前处理
        """
        len1, len2 = len(word1), len(word2)
        if len1 == 0:
            return len2
        if len2 == 0:
            return len1
        
        dp = []
        for _ in range(len1 + 1):
            dp.append([None] * (len2 + 1))

        def dfs(i, j):
            # base case
            # if word1 is empty, need to insert j times
            if i == 0:
                return j
            if j == 0:
                return i

            if dp[i][j] is not None:
                return dp[i][j]

            # if is match
            if word1[i - 1] == word2[j - 1]:
                res = dfs(i - 1, j - 1)
            else:
                insert = dfs(i, j - 1)
                delete = dfs(i - 1, j)
                replace = dfs(i - 1, j - 1)
                res = min(insert, delete, replace) + 1

            dp[i][j] = res
            return res

        return dfs(len1, len2)