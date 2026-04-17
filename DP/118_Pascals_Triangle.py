class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        time: O(numRows^2): we will generate 1+2+3+...+numRows = numRows*(numRows+1)/2 elements
        space: O(numRows^2): we will store numRows*(numRows+1)/2 elements
        """
        ans = []
        for row in range(numRows):
            curr_row = []
            for j in range(row + 1):
                if j == 0 or j == row:
                     curr_row.append(1)
                else:
                    above_left = ans[row - 1][j - 1]
                    above_right = ans[row - 1][j]
                    curr_row.append(above_left + above_right)
            ans.append(curr_row)
        return ans

        