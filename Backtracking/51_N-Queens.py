class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]

        time: O(N!)
        space: O(N^2) since we created board to store res
        """

        col = set()
        # r + c stays same
        posDiag = set()
        # r - c stays same
        negDiag = set()

        res = []
        board = []
        for i in range(n):
            row = ['.'] * n
            board.append(row)
        
        def backtrack(r):
            if r == n:
                copy = []
                for row in board:
                    copy.append(''.join(row))
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return res





