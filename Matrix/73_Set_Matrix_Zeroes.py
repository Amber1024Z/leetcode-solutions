class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        
        time: O(n^2)
        space: O(1)
        """
        
        # use the first row and first column as markers to record which rows and columns should be set to zero
        rows, cols = len(matrix), len(matrix[0])
        # rowZero record whether first row has 0
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # use first row to mark down this col need change to 0
                    matrix[0][c] = 0

                    # except first row, use first col to markdown which r will be 0
                    if r > 0:
                        matrix[r][0] = 0
                    # if first row have 0, markdown to 0
                    else:
                        rowZero = True

        # skip first row and first col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # deal frist col
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # deal first row
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0