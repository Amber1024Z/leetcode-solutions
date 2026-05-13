from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        
        time: O(N + M), N = len(s), M = len(t), we need O(M) time to build t_count, then we need O(N) time to move r and l pointer, each pointer will move at most N times
        space: O(N + M), for counter
        """
        t_count = Counter(t)
        w_count = Counter()
        # have: how many char in t we have in current window, need: how many char in t we need to have
        have, need = 0, len(t_count)
        res = ''
        l = 0

        for r in range(len(s)):
            w_count[s[r]] += 1

            if w_count[s[r]] == t_count[s[r]]:
                have += 1
            
            while have == need:
                # update res, check whether current window is smaller than res, if res is empty, we also update res
                if not res or (r - l + 1) < len(res):
                    res = s[l : r + 1]
                w_count[s[l]] -= 1
                # if count of s[l] in w_count is less than count of s[l] in t_count, means we no longer have enough s[l] in current window
                if w_count[s[l]] == t_count[s[l]] - 1:
                    have -= 1

                l += 1

        return res