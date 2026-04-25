class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.

        time: O(m, n)
        space: O(1), in-place modification
        """

        num_rows, num_cols = len(board), len(board[0])

        def dfs(r, c):
            # we only visited O
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols or board[r][c] != 'O':
                return
            
            board[r][c] = 'S'

            # only O on edge or any 'O' close to edge 'O' will be marker as 'S'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(num_rows):
            for c in range(num_cols):
                # we only search 'O' on edge
                if (r == 0 or r == num_rows - 1 or c == 0 or c == num_cols - 1) and board[r][c] == 'O':
                    dfs(r, c)

        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'

        