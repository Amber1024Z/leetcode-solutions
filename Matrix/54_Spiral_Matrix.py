class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        
        time: O(n^2)
        space: O(1) without result, O(n^2) with result
        """
        
        result = []

        while matrix:
            # step 1: take out first row
            result += matrix.pop(0)

            # step 2: take out last col, read from top to end
            # row.pop(): return last element of each row
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # step 3: take out last row, read from tail to head
            if matrix:
                result += matrix.pop()[::-1]

            # step 4: take out first col, read from end to top
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result
