class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int

        time: on each row after place queen, for next row avaliable space will decrease, overall is O(n!)
        space: O(n), max depth of stack is length of row of board.
        """
        col = set()
        # r + c stays same
        posDiag = set()
        # r - c stays same
        negDiag = set()
        
        self.count = 0
        
        def backtrack(r):
            if r == n:
                self.count += 1
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return self.count