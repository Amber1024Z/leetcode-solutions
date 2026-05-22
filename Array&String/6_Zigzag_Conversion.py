class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str

        time: O(n)
        space: O(1)
        """

        if numRows == 1:
            return s
            
        ans = [''] * numRows
        curr_row, going_down = 0, False

        for c in s:
            ans[curr_row]  += c
            # if it's first or last row, we should change direction
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down

            if going_down:
                curr_row += 1
            else:
                curr_row -= 1

        return ''.join(ans)