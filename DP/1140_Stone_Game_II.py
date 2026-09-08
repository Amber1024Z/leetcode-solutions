class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int

        time: O(n^3), double for loop nested 1 for loop
        space: O(n^2)
        """
        
        # dp[i][m] represent from piles[i:] with m, max stones curr player can get
        # curr player max stone = remain stone - max opponent get from next round
        # dp[i][M] = suffix[i] - dp[next_i][next_M]

        n = len(piles)

        # since we take stone in the first X remaining piles, calculate suffix from end to start
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        dp = []

        # 1 <= M <= n, we can use (n + 1) size to easier demonstrate dp[i][M]
        for _ in range(n + 1):
            dp.append([0] * (n + 1))

        # opponent_best = dp[i + X][max(M, X)]
        # dp[i][M] = suffix[i] - opponent_best
        # thus dp[i][M] relys on dp[i + X], so i iterate from end to start
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                # if curr player able to take all rest
                # n - i represent remain piles number
                if 2 * M >= n - i:
                    dp[i][M] = suffix[i]

                else:
                    max_val = 0

                    # try different X to get best choile
                    for X in range(1, 2 * M + 1):

                        opponent_best = dp[i + X][max(M, X)]
                        curr_best = suffix[i] - opponent_best

                        max_val = max(max_val, curr_best)

                    dp[i][M] = max_val
        
        # from idx = 0, with initially M = 1, max stone alice can get
        return dp[0][1]



