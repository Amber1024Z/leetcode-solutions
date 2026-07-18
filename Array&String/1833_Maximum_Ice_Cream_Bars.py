class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int

        time: O(n+m), iterate on the input array also iterate on bukcet.
        space: O(m), size for bucket
        """
        
        n = len(costs)
        ans = 0
        max_cost = max(costs)

        bucket = (max_cost + 1) * [0]

        for cost in costs:
            bucket[cost] += 1

        # price constraints: 1 <= costs[i], cost start from 1
        for cost in range(1, max_cost + 1):
            if not bucket[cost]:
                continue
            if cost > coins:
                break

            """
            bucket[3] = 2, coins = 30, 30 // 3 = 10, but still we only able to buy 2
            bucket[3] = 10, coins = 8, 8 // 3 = 2, also only able to buy 2
            count limited by coins also number of curr price's frequency
            """
            count = min(bucket[cost], coins // cost)
            coins -= cost * count
            ans += count

        return ans

