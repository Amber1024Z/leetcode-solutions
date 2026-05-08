class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        
        time: O(n^2)
        space: O(1)
        """

        # 90 degree: transpose + reverse row
        self.transpose(matrix)
        self.reverse(matrix)

    # row to col, col to row, Flip diagonally
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            # we won't change number on diagonal(i, j), thus i + 1
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse(self, matrix):
        n = len(matrix)

        for i in range(n):
            # Only traverse the first half of each line
            for j in range(n // 2):
                # -j-1 means opposite position for j: 0 -> -1, 1 -> -2, 2-> -3
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
                

