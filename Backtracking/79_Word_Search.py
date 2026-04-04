class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        
        time: we have m*n size board, each letter we will give a try, for each letter we have 3 directions
        to explore, overall is O(m * n * (3 ^ L)), L is length of word
        space: O(L)
        """

        numRow, numCol = len(board), len(board[0])

        def backtrack(row, col, i):
            if i == len(word):
                return True

            if (row < 0) or (row >= numRow) or (col < 0) or (col >= numCol) or board[row][col] != word[i]:
                return False

            temp = board[row][col]
            board[row][col] = '#'

            res = (backtrack(row + 1, col, i + 1) or
                    backtrack(row - 1, col, i + 1) or
                    backtrack(row, col + 1, i + 1) or
                    backtrack(row, col - 1, i + 1))

            board[row][col] = temp
            return res
            
        for r in range(numRow):
            for c in range(numCol):
                if backtrack(r, c, 0):
                    return True

        return False
