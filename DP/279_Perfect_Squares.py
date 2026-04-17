class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int

        time: O(n * sqrt(n)) we have two nested loops, the outer loop iterates through each number from 1 to
        n (O(n)), and the inner loop iterates through each square number less than or equal to the current 
        number (O(sqrt(n))).

        space: O(n) we use a dp array of size n + 1 to store the minimum number of perfect squares for each number from 0 to n.
        """
        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        # calculate possible square nums <= n
        square_nums = []
        i = 1
        while  i * i <= n:
            square_nums.append(i * i)
            i += 1

        for i in range(1, n + 1):
            for num in square_nums:
                # if the current square number is greater than the current index i, we can break
                if i < num:
                    break
                
                # dp[i - num] + 1 means we take the current square number and add 1 to the result of dp[i - num]
                dp[i] = min(dp[i], dp[i - num] + 1)

        return dp[-1]
        