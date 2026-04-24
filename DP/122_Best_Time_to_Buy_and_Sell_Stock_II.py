class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        ex: [1, 5, 10], we can buy at 1, sell at 5, then buy at 5, sell at 10, total profit is 9, or we can 
        buy at 1, sell at 10, total profit is also 9, so as long as next day price is higher, we will doing the trade

        (a3 - a1) = (a3 - a2) + (a2 - a1)

        time: O(n), where n is the length of the input array
        space: O(1)

        """
        # as long as next day price is higher, we will doing the trade
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i]- prices[i - 1]

        return max_profit