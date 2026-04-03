class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        
        time: for length = n string, ex: 'aaaa' has 3 gaps, can choose cut or not, thus will be 2^n, each time need to check whether is palindrome, will takes O(n), thus overall is n * (2^n)
        space: O(n)
        """
        res = []
        n = len(s)

        def palindrome(s):
            return s == s[::-1]

        def backtrack(curr, start):
            if start == n:
                res.append(curr[:])
                return

            # i represents cut point
            for i in range(start, n):
                substring = s[start: i+1]
                # Check if it is a palindrome, then continue
                if palindrome(substring):
                    curr.append(substring)
                    backtrack(curr, i + 1)
                    curr.pop()

        backtrack([], 0)
        return res

