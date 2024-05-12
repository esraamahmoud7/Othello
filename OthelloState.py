# from OthelloBoard import OthelloBoard

##If a player cannot outflank and flip at least one opposing disk, they miss their turn and their opponent moves again.
## to check check no possible moves and there are 2 colors in board

class OthelloGameState:
    def __init__(self, Board):
        self.current_player = 'B'
        self.board = Board
        self.human_turn = True

    def switch_player(self):
        if self.current_player == 'B':
            self.current_player = 'W'
            self.human_turn = False
        else:
            self.current_player = 'B'
            self.human_turn = True

    def Calculate_Score(self):
        black_Score = 0
        white_Score = 0
        for row in self.board.board:
            for cell in row:
                if cell == 'B':
                    black_Score += 1
                elif cell == 'W':
                    white_Score += 1
        print("Black score:", black_Score)
        print("White score:", white_Score)

    def Possible_Moves(self):
        valid_Moves = []
        # Check all possible moves
        for row in range(8):
            for col in range(8):
                if self.board.board[row][col] == '_':
                    # Check if the move is valid
                    if self.is_valid_move(row, col):
                        valid_Moves.append((row, col))
        return valid_Moves

    def is_valid_move(self, row, col):
        flag = False
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in AvailDir:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and self.board.board[r][c] != '_' and self.board.board[r][c] != self.current_player:
                r, c = r + dr, c + dc
                flag = True

            if flag and 0 <= r < 8 and 0 <= c < 8 and self.board.board[r][c] == self.current_player:
                return True
            flag = False

        return False

    def Utility(self, row, col):
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        flip = []
        for dr, dc in AvailDir:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and self.board.board[r][c] != '_' and self.board.board[r][c] != self.current_player:
                flip.append((r, c))
                r += dr
                c += dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board.board[r][c] == self.current_player:
                return len(flip)
        return 0
