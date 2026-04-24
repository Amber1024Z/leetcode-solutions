class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int

        time: O(n^2), where n is the number of rows in the triangle
        space: O(n), where n is the number of rows in the triangle
        """

        n = len(triangle)

        dp = triangle[-1]

        # update from the second last row to the top row, because the minimum path sum of the current row depends on the minimum path sums of the next row
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        return dp[0]