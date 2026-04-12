class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True

        allowed_chars = ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        board_len = len(board)
        if board_len != 9:
            return False
        
        for each_sec in board:
            if len(each_sec) != 9:
                return False

            temp = list(filter(lambda x: x not in ['.'], each_sec))
            temp2 = list(set(temp))

            if len(temp) != len(temp2):
                return False

            for i in range(len(each_sec)):
                if each_sec[i] not in allowed_chars:
                    return False


        grids = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grids.append(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])

        for each_grid in grids:
            
            temp = list(filter(lambda x: x not in ['.'], each_grid))
            temp2 = list(set(temp))

            if len(temp) != len(temp2):
                return False

            for j in range(len(each_grid)):
                if each_grid[j] not in allowed_chars:
                    return False
                

        transpose_board = list(map(list, zip(*board)))        
        for each_t_sec in transpose_board:
            if len(each_t_sec) != 9:
                return False

            temp = list(filter(lambda x: x not in ['.'], each_t_sec))
            temp2 = list(set(temp))

            if len(temp) != len(temp2):
                return False

        return res