class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        
        time:  since the board is always 9 * 9, we can consider it as constant time
        space: O(1), we use 3 set to record rows, cols and boxes, each set has at most 9 elements, we can consider it as constant spaceO(1)
        """

        N = 9
        # use set to avoid duplicate
        rows = [set() for _ in range(N)]
        

        cols = [set() for _ in range(N)]
        # divide 3 * 3 board into 9 small box
        boxes = [set() for _ in range(N)]

        # itearte all locations
        for r in range(N):
            for c in range(N):
                val = board[r][c]

                # skip empty block
                if val == '.':
                    continue

                # check rows
                if val in rows[r]:
                    return False
                else:
                    rows[r].add(val)

                # check col
                if val in cols[c]:
                    return False
                else:
                    cols[c].add(val)

                # check small box, 0-8
                # row: r // 3, col: c // 3, idx = row * cols + cols
                idx = (r // 3) * 3 + (c // 3)
                if val in boxes[idx]:
                    return False
                else:
                    boxes[idx].add(val)


        return True

                

