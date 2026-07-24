class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int

        time: O(nlog(S)), search range is S = sum(weights) - max(weights), for each capacity we will call get_days, takes O(n).

        space: O(1)
        """
        
        # capacity can't be smaller than package weight, thus lower boundary must be max weight
        left = max(weights)
        right = sum(weights)

        # with capacity C, how many days we need to ship
        def get_days(capacity):
            need = 1
            curr_weight = 0

            for w in weights:
                if curr_weight + w > capacity:
                    # curr w > capacity, need to move on next day
                    need += 1
                    # curr w become curr_weight for next day begins
                    curr_weight = w
                else:
                    curr_weight += w

            return need

        ans = float('inf')

        while left <= right:
            m = (left + right) // 2

            if get_days(m) <= days:
                # curr capacity can ship, but we still need to find smaller ans
                ans = min(ans, m)
                right = m - 1
            else:
                left = m + 1

        return ans
