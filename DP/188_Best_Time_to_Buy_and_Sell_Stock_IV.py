class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        
        # if k exceed days // 2, we can trade each time when price goes up
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

        costs = [float('inf')] * k
        profits = [0] * k

        for price in prices:
            for j in range(k):
                if j > 0:
                    prev_profit = profits[j-1]
                else:
                    prev_profit = 0
                # The cost of the jth trade = current price – profit from the previous trade
                costs[j] = min(costs[j], price - prev_profit)
                # Total profit from the jth transaction = current price – actual net expenditure for the jth transaction
                profits[j] = max(profits[j], price - costs[j])

        return profits[-1]