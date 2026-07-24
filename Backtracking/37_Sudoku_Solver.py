class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.

        time: O(1), without pruning, consider first row, we have 9! options, 9 * 8 * 7..., we have 9 rows, 
        worst we have to try 9 * (9!) times.
        space: O(1) for sets
        """
        
        # initialize sets for rows, cols, boxes
        rows = []
        for _ in range(9):
            rows.append(set())

        cols = []
        for _ in range(9):
            cols.append(set())

        boxes = []
        for _ in range(9):
            boxes.append(set())

        # collect all empty cells
        blank_cells = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                else:
                    blank_cells.append((r,c))

        def backtrack(idx):
            if idx == len(blank_cells):
                return True

            r, c = blank_cells[idx]

            box_idx = (r // 3) * 3 + (c // 3)

            # enter num from 1 - 9
            for num in range(1, 10):
                ch = str(num)
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_idx]:
                    # make choice is curr num not in set
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_idx].add(ch)

                    # backtrack next emepty idx
                    # if curr choice is not right, will return false, enter line 58 redo choice
                    if backtrack(idx + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_idx].remove(ch)

            # if tried all 1-9 are not correct, report it to parent
            return False

        backtrack(0)