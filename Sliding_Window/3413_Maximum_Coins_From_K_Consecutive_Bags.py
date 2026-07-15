class Solution(object):
    def maximumCoins(self, coins, k):
        """
        :type coins: List[List[int]]
        :type k: int
        :rtype: int

        best solution whether start align with L or end align with R, need to check both

        time: O(nlogn), sort costs nlogn, 2 pointers costs O(n), only move from left to right
        space: O(n) for reversed coins.
        """

        # helper to find start align with all L, max coins we can get
        def align_left(coins):
            # sort base on L
            coins.sort(key = lambda x: x[0])

            max_coins = 0
            curr_sum = 0
            # l means idx for interval, after calculate curr interval, l += 1
            l = 0

            for r in range(len(coins)):
                # each round r won't move, always point to this round first interval, l will move to right
                start = coins[r][0]
                # end calculate base on size of k, max interval end we can include
                end = start + k - 1

                # calculate curr sum for curr interval 
                while l < len(coins) and coins[l][1] <= end:
                    curr_sum += (coins[l][1] - coins[l][0] + 1) * coins[l][2]
                    # l point to next interval need to check
                    l += 1

                # some interval may partialy includ, or curr interval is larger than k
                partial_sum = 0
                if l < len(coins) and coins[l][0] <= end:
                    partial_sum = (end - coins[l][0] + 1) * coins[l][2]

                # calculate curr + partial
                max_coins = max(max_coins, curr_sum + partial_sum)

                # to calculate next round, curr_sum should - first interval's total
                curr_sum -= (coins[r][1] - coins[r][0] + 1) * coins[r][2]

                # when l <= r, means last round, last interval's end base on l <= next round start intervals's beginning, let curr_sum reset, also l = r + 1, means l move to next inrerval need to check
                if l <= r:
                    # l point to next interval need to check base on line 30, if first range'end over k, then will not enter while(line 27), l still point to first range, not second.
                    # or first calculation include all coins in first interval, but end didn't reach second interval's beginning
                    # both situation lead l = r + 1, next round l and r point to same interval, if curr interval can be include, will enter while (line 27) let l +=1 to calculate partial, or enter line 33 to calculate partial.
                    l = r + 1
                    curr_sum = 0 

            return max_coins

        align_left_ans = align_left(coins)
        reversed_coins = []

        for coin in coins:
            l, r, c = coin
            new_l = -r
            new_r = -l
            # after revered, new_l > new_r, thus new_r should on right
            # [3, 10] -> [-10, -3]
            reversed_coins.append([new_l, new_r, c])

        align_right_ans = align_left(reversed_coins)

        return max(align_left_ans, align_right_ans)
