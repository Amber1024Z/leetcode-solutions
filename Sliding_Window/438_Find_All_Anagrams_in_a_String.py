from typing import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]

        time: O(n)
        space: O(K), K is the size of p, also size of counter
        """
        k = len(p)
        ans = []
        p_count = Counter(p)
        w_count = Counter()
        l = 0

        for r in range(len(s)):
            w_count[s[r]] += 1
            # when window size is k, check if w_count and p_count are the same, if same, add l to ans, then narrow down window by move l and update w_count
            if (r - l + 1) == k:
                if w_count == p_count:
                    ans.append(l)
                # narrow down window by move l and update w_count
                w_count[s[l]] -= 1
                # if count of s[l] is 0, remove it from w_count to make sure w_count and p_count can be compared
                if w_count[s[l]] == 0:
                    del w_count[s[l]]

                l += 1

        return ans
