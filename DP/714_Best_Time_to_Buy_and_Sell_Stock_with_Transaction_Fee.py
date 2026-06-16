class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        
        time: O(n)
        space: O(n)
        """
        n = len(prices)
        
        # on ith day, hold a stock, max profit I have so far
        hold = [0] * n
        # on ith day, without any stock, max profit I have so far
        free = [0] * n

        # on day 1, in oreder to 'Have' a stock, we must buy
        hold[0] = -prices[0]

        for i in range(1, n):
            # on each day, I can choose doing nothing if yesterday I alredy have a stock in hand, or yesterday
            # I don't have any stock, I will buy stock today
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            # I can choose sell stock I have right now, or doing nothing like prev day
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)

        return free[-1]