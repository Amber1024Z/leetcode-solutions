class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool

        time: O(n^2)
        space: O(n^2)
        """

        n = len(piles)

        dp = []

        for _ in range(n):
            dp.append([0] * n)

        # take left, net = piles[left] - dp[l+1][r]
        # take right, net = piles[right] - dp[l][r - 1]

        for i in range(n):
            dp[i][i] = piles[i]

        for diff in range(1, n):
            # left + diff = right, left = right - diff, max idx for right is n - 1, thus 
            # left <= n - 1 - diff
            for left in range(n - diff):
                right = left + diff

                dp[left][right] = max(
                    piles[left] - dp[left + 1][right], piles[right] - dp[left][right - 1]
                    )

        return dp[0][n - 1] > 0

        