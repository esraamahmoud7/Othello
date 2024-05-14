# from OthelloBoard import OthelloBoard

##If a player cannot outflank and flip at least one opposing disk, they miss their turn and their opponent moves again.
## to check check no possible moves and there are 2 colors in board
import copy



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
        return black_Score, white_Score
        # print("Black score:", black_Score)
        # print("White score:", white_Score)

    def Possible_Moves_User(self):
        valid_Moves = []
        # Check all possible moves
        for row in range(8):
            for col in range(8):
                if self.board.board[row][col] == '_':
                    # Check if the move is valid
                    if self.is_valid_move_User(row, col):
                        valid_Moves.append((row, col))
        return valid_Moves

    def is_valid_move_User(self, row, col):
        flag = False
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in AvailDir:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and self.board.board[r][c] != '_' and self.board.board[r][c] != 'B':
                r, c = r + dr, c + dc
                flag = True

            if flag and 0 <= r < 8 and 0 <= c < 8 and self.board.board[r][c] == 'B':
                return True
            flag = False

        return False

    def alpha_beta_Purned(self, first,testBoard, depth, alpha, beta, isComputer):
        # for testBoard to avoid change in original board
        TestedBoard = testBoard
        # if depth == 0 or board.isGameOver():  # go depth to leaf or gameOver
        if depth == 0:  # go depth to leaf or gameOver
            # when arrive to leaf you need to call unitlityFunction and return None for move can't make
            # moves any_more
            return self.Utility(testBoard), None
        if first:
            first=False
            testBoard = self.board

        if isComputer:
            # if computer play gave a list for all valid moves can machine make
            validMoves = self.Possible_Moves_Computer(testBoard)
            # init maxVal with negative value at first to start evaluate valid moves
            maxVal = -10000
            bestMove = None  # at first time best move is none
            for move in validMoves:
                # ------------------------------------------
                # make a deep cop for board to test alpha
                TestedBoard = copy.deepcopy(testBoard)
                TestedBoard = TestedBoard.update_Board_Computer(TestedBoard,move[0], move[1], 'W')  # make move in test board
                # player turn
                evaluate, _ = self.alpha_beta_Purned(False,TestedBoard, depth - 1, alpha, beta, False)
                if evaluate > maxVal:  # if evaluate val is bigger than maxVal so make maxVal = eval alpha take max
                    maxVal = evaluate
                    bestMove = move
                    alpha = max(alpha, evaluate)
                    if alpha >= beta:
                        break  # when alpha is bigger than betta stop this branch don't continue
            return maxVal, bestMove  # return max and the move
        else:  # every thing we make in alpha do with beta but with min not max
            validMovs = self.Possible_Moves_User()
            minVal = 10000
            bestMove = None
            for move in validMovs:
                TestedBoard = copy.deepcopy(testBoard)
                TestedBoard = TestedBoard.update_Board_Computer(TestedBoard,move[0], move[1], 'B')
                evaluate, _ = self.alpha_beta_Purned(False,TestedBoard, depth - 1, alpha, beta, True)
                if evaluate < minVal:
                    minVal = evaluate
                    bestMove = move
                    beta = min(beta, evaluate)
                    if beta <= alpha:
                        break
            return minVal, bestMove

    def Utility(self, testBoard):
        black_Score = 0
        white_Score = 0
        for row in testBoard:
            for cell in row:
                if cell == 'B':
                    black_Score += 1
                elif cell == 'W':
                    white_Score += 1
        return white_Score - black_Score

    def Possible_Moves_Computer(self, TestBoard):
        valid_Moves = []
        # Check all possible moves
        for row in range(8):
            for col in range(8):
                if TestBoard[row][col] == '_': ## problem in thisss
                    # Check if the move is valid
                    if self.is_valid_move_Computer(row, col, TestBoard):
                        valid_Moves.append((row, col))
        return valid_Moves  # Corrected indentation

    def is_valid_move_Computer(self, row, col, TestBoard):
        flag = False
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in AvailDir:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and TestBoard[r][c] != '_' and TestBoard[r][c] != 'W':
                r, c = r + dr, c + dc
                flag = True

                if flag and 0 <= r < 8 and 0 <= c < 8 and TestBoard[r][c] == 'W':
                    return True

                flag = False

        return False

        # AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # flip = []
        # for dr, dc in AvailDir:
        #     r, c = row + dr, col + dc
        #     while 0 <= r < 8 and 0 <= c < 8 and self.board.board[r][c] != '_' and self.board.board[r][c] != self.current_player:
        #         flip.append((r, c))
        #         r += dr
        #         c += dc
        #     if 0 <= r < 8 and 0 <= c < 8 and self.board.board[r][c] == self.current_player:
        #         return len(flip)
        # return 0
