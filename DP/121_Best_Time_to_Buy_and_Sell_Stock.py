class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        time: O(n), where n is the length of the input array
        space: O(1)
        """

        if not prices and len(prices) < 2:
            return 0

        min_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] - min_price > profit:
                profit = prices[i] - min_price
            if prices[i] < min_price:
                min_price = prices[i]

        return profit