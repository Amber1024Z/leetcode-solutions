class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        time: log(m * n)
        space: O(1)
        """
        if not matrix or not matrix[0]:
            return False

        num_rows, num_cols = len(matrix), len(matrix[0])
        # flattern matrix to 1 dimension for bianry search
        left, right = 0, (num_rows * num_cols) - 1

        while left <= right:
            mid = (left + right) // 2
            # convert idx to row, col
            # mid // cols means skip how many rows, mid % cols means position in curr row
            mid_val = matrix[mid // num_cols][mid % num_cols]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

            

        