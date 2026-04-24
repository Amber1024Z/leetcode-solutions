class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        time: O(s * n), n is amount of money, s is the number of coins
        space: O(n) we use a dp array of size n + 1 to store the minimum number of coins for each amount from 0 to n
        """

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            # start from coin because we cannot make change for amounts less than the coin value
            for i in range(coin, amount + 1):
                # dp[i - coin] + 1 means we take the current coin and add 1 to the result of dp[i - coin]
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[-1] != float('inf'):
            return dp[-1]
        else:
            return -1
