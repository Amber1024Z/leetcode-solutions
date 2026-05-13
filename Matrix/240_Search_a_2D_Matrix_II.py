class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        start from right up cornner, ex: if start from 15, target < 15, we know we should search on left, if 
        target > 15, we should search up down.
        
        time: O(m + n), m is number of rows, n is number of cols
        space: O(1)
        """

        rows, cols = len(matrix), len(matrix[0])

        # start from right upper corner
        row, col = 0, cols - 1
        while 0 <= row < rows and 0 <= col < cols:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False