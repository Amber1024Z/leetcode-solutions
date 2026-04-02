class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        if n <= 1:
            return 0

        # scan from left to right
        # left_profits[i] means from 0 to i, max profit we can find
        left_profits = [0] * n 
        min_price = prices[0]

        for i in range(1, n):
            # maintain yesterday's profit, or sell today(prices[i] - min_price)
            left_profits[i] = max(left_profits[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        # scan from right to left
        # right_profits[i] means from i to last day, max profit we can find
        # right need 1 more space, because when we combine, i will become n - 1, 
        # curr_total = left_profits[n - 1] + right_profits[n]
        right_profits = [0] * (n + 1)
        max_price = prices[-1]

        for i in range(n - 2, -1, -1):
            # maintain future max profit, or buy today(future max price - prices[i])
            right_profits[i] = max(right_profits[i + 1], max_price - prices[i])
            max_price = max(max_price, prices[i])

        # find cut point, combine 2 transactions
        max_total = 0
        for i in range(n):
            # first transaction on day i, second transaction start at day i + 1
            curr_total = left_profits[i] + right_profits[i + 1]
            max_total = max(max_total, curr_total)

        return max_total