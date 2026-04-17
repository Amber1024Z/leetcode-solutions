class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        time: O(n * m * k) where n is the length of the string s, m is the number of words in the wordDict, 
        and k is the average length of the words in the wordDict. We have two nested loops: the outer loop 
        iterates through each character in the string (O(n)), and the inner loop iterates through each word in the 
        wordDict (O(m)). For each word, we check if it matches a substring of s, which takes O(k) time.

        space: O(n) for the dp array, where n is the length of the string s. 
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                w_len = len(word)
                # i must be greater than or equal to the length of the word, and dp[i - w_len] must be True, and the substring s[i - w_len : i] must be equal to the word
                if i >= w_len and dp[i - w_len] and s[i - w_len : i] == word:
                    dp[i] = True
                    break
            
        return dp[-1]