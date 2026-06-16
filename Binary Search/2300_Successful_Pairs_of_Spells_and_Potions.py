class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]

        time: for sort takes mlogm, m is size for potions, iterate n times for binary seach, n
        is size for spells, this part will takes nlogm, overall is O((m + n) * logm)

        space: O(m) for sorted, will create a new array
        """
        ans = []
        sorted_p = sorted(potions)
        n = len(potions)

        for s in spells:
            l, r = 0, n - 1

            while l < r:
                m = (l + r) // 2

                # m could be ans, can't skip
                if sorted_p[m] * s >= success:
                    r = m
                else:
                    l = m + 1
            
            # will stop when l == r
            if sorted_p[l] * s >= success:
                count = n - l
            # otherwise no potions satisfiled
            else:
                count = 0
            
            ans.append(count)

        return ans




                