class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        1. <2 : dead
        2. 2 or 3: live
        3. > 3: dead
        4. =3 : dead to live

        if is dead to live set to 2, if is live to dead, set to -1
        thus abs(r, c) == 1 will turn current result
        
        time: O(m  * n)
        space: O(1)
        """
        # find all 8 neighbors position
        neighbors = [
            (1, 0),  
            (1, -1), 
            (0, -1), 
            (-1, -1),
            (-1, 0),  
            (-1, 1), 
            (0, 1),  
            (1, 1)   
        ]
        
        rows = len(board)
        cols = len(board[0])

        # iterate all cells 
        for row in range(rows):
            for col in range(cols):

                # for each cell count its live neighbors
                live_neighbors = 0

                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]

                    # first check whether is a valid position
                    if (r >= 0 and r < rows) and (c >= 0 and c < cols) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # update game rules
                # live neighbors < 2 or > 3, live to dead
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                # if live neighbor = 3, dead to live
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                # 2 or 1 means alive
                if board[row][col] > 0:
                    board[row][col] = 1
                # -1 or 0 means dead
                else:
                    board[row][col] = 0




        