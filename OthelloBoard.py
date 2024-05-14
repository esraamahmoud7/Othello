# from OthelloState import OthelloGameState


# State Representation
# OthelloBoard.py


class OthelloBoard:
    def __init__(self):
        self.board = [['_' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.board[4][4] = 'W'

    def __getitem__(self, key):
        return self.board[key]

    def has_empty_places(self):
        for row in self.board:
            if '_' in row:
                return True
        return False

    def print_board(self, current_player):
        print("Current Player:", current_player)
        print("   0 1 2 3 4 5 6 7")
        print("  -----------------")
        for i, row in enumerate(self.board):
            print(str(i) + "|", ' '.join(row))
        print("\n")

    # (1, 0): Downward in same column.
    # (-1, 0): Upward in same column.
    # (0, 1): Rightward ins ame row.
    # (0, -1): Leftward in same row.
    # (1, 1): Diagonal down-right
    # (-1, -1): Diagonal up-left
    # (1, -1): Diagonal down-left
    # (-1, 1): Diagonal up-right

    # Update Board after each move
    def update_Board(self, row, col, current_player):
        self.board[row][col] = current_player
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)] #(1, 1), (-1, -1), (1, -1), (-1, 1)
        for dr, dc in AvailDir:
            flip = []
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != '_' and self.board[r][c] != current_player:
                flip.append((r, c))
                # still move in same direction untill we find our own piece or reach to boundry
                r += dr
                c += dc
            # checks if the indices r and c are within the bounds of the board
            # reach to disk of current player so start flip the disk
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == current_player:
                for r, c in flip:
                    self.board[r][c] = current_player

    def update_Board_Computer(self,Board,row, col, current_player):
        Board[row][col] = current_player
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)] #(1, 1), (-1, -1), (1, -1), (-1, 1)
        for dr, dc in AvailDir:
            flip = []
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and Board[r][c] != '_' and Board[r][c] != current_player:
                flip.append((r, c))
                # still move in same direction untill we find our own piece or reach to boundry
                r += dr
                c += dc
            # checks if the indices r and c are within the bounds of the board
            # reach to disk of current player so start flip the disk
            if 0 <= r < 8 and 0 <= c < 8 and Board[r][c] == current_player:
                for r, c in flip:
                    Board[r][c] = current_player
        return Board

    def show_possible_moves(self, vaild_moves,current_player):
        for node in vaild_moves:
            self.board[node[0]][node[1]] = 'X'
        self.print_board(current_player)

    def remove_possible_moves(self, vaild_moves):
        for node in vaild_moves:
            self.board[node[0]][node[1]] = '_'


    # def isGameOver(self):
    #     if not self.has_empty_places() or not self
    #         return True

    # def get_valid_moves(self):
    #     valid_moves=[]
    #     for row in range(8):
    #         for col in range(8):
    #             if self.board[row][col] == ' ' and self.is_valid_move(row, col):
    #                 valid_moves.append((row, col))
    #     return valid_moves
    # (row,column).
    # (1, 0): Downward in same column.
    # (-1, 0): Upward in same column.
    # (0, 1): Rightward ins ame row.
    # (0, -1): Leftward in same row.
    # (1, 1): Diagonal down-right
    # (-1, -1): Diagonal up-left
    # (1, -1): Diagonal down-left
    # (-1, 1): Diagonal up-righ
    # def is_valid_move(self, row, col):
    #     directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    #     for validR, validC in directions:
    #         r, c = row + validR, col + validC
    #         #in board boundry
    #         if not (0 <= r < 8 and 0 <= c < 8):
    #             continue
    #             ##??????
    def has_white_nodes(self):
        for row in self.board:
            if 'W' in row:
                return True
        return False

    def has_black_nodes(self):
        for row in self.board:
            if 'B' in row:
                return True
        return False

