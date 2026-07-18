class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int

        number can eaqul to neighbors, not allow increasing or decreasing sequence

        A < B > C, A > B < C, valid pattern

        time: O(mn), m=r-l+1
        space: O(m)
        """

        MOD = 10**9 + 7
        # m is counter for valid number we can choose

        m = r - l + 1
        """
        dp0 represent previous number fell down and landed here. prev > curr
        # dp1 represent previous number increace to here. prev < curr
        # If the previous cycle saw a rise, this round must see a fall; if the previous cycle saw a fall, this one must see a rise.
        
        dp0[x] represent curr number is x, number has fallen to x
        dp1[x] represent curr number is x, number has rise to x

        When the length is 1, there is only one way to arrange each digit.
        """
        dp0 = [1] * m
        dp1 = [1] * m

        for _ in range(n - 1):
            # calculate prefix sum for dp0, represents combo prefix sum
            # add 0 ay beginning for easier idx calculate
            sum0 = [0]
            for x in dp0:# dp0 = [1, 1, 1]
                sum0.append(sum0[-1] + x)

            sum1 = [0]
            for x in dp1:
                sum1.append(sum1[-1] + x)

            # calculate dp for next round
            next_dp0 = [0] * m
            next_dp1 = [0] * m

            for x in range(m):
                # next_dp0[x], is fall to x, prev > x. Also prev need to 'rise' to prev, so we take combo number from sum1. Also next round need to be 'rise'
                # x represents xth position in the list of valid numbers
                # sum1[k], k represents number of digit, not idx, so we need to +1 to align
                # Remove the '<=x' part, and what remains is the '>x' part
                # since we need find number greater than x, left bounday is x + 1, right boundary is m - 1.
                total_greater = sum1[m] - sum1[x + 1]
                next_dp0[x] = total_greater % MOD

                # prev need to < x, left boundary is 0, right boundary is x - 1.
                # we need find x's left value, so should be x - 1 + 1. right boundary + 1 - left boundry, x - 1 +1 = x.
                total_smaller = sum0[x]
                next_dp1[x] = total_smaller % MOD

            dp0 = next_dp0
            dp1 = next_dp1
        
        return (sum(dp0) + sum(dp1)) % MOD




            





        