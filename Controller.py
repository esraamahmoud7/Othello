# Controller.py
from random import choice

from OthelloBoard import OthelloBoard
from OthelloState import OthelloGameState


class Game:
    def StartGame(self):
        newBoard = OthelloBoard()
        GameState = OthelloGameState(newBoard)

        print("Game Start\n")

        # newBoard.print_board(GameState.current_player)
        # newBoard.update_Board(2, 3, GameState.current_player)
        # newBoard.print_board(GameState.current_player)
        # GameState.Calculate_Score()
        # GameState.switch_player()
        # newBoard.update_Board(2, 2, GameState.current_player)
        # newBoard.print_board(GameState.current_player)

        # Controller
        while newBoard.has_empty_places():

            if GameState.human_turn:
                possible_moves = GameState.Possible_Moves()
                newBoard.show_possible_moves(possible_moves, GameState.current_player)
                row = int(input("Enter row: "))
                col = int(input("Enter col: "))

                while newBoard.board[row][col] == '_' or (row, col) not in possible_moves or newBoard.board[row][
                    col] != 'X':
                    print("Invalid move")
                    newBoard.remove_possible_moves(possible_moves)
                    newBoard.show_possible_moves(possible_moves, GameState.current_player)
                    row = int(input("Enter row: "))
                    col = int(input("Enter col: "))

                else:
                    # out possible moves
                    newBoard.remove_possible_moves(possible_moves)
                    newBoard.update_Board(row, col, GameState.current_player)
                    # newBoard.print_board(GameState.current_player)
                    GameState.Calculate_Score()
                    GameState.switch_player()
                    newBoard.print_board(GameState.current_player)

            else:
                # Computer Turn
                possible_moves = GameState.Possible_Moves()
                print("Possible moves: ", possible_moves)
                evaluation = []
                for move in possible_moves:
                    evaluation.append(GameState.Utility(move[0], move[1]))

                max_value = max(evaluation)
                max_index = evaluation.index(max_value)
                best_move = possible_moves[max_index]

                if len(possible_moves) == 0:
                    print("Game Over")
                    GameState.switch_player()
                    break
                row, col = choice(possible_moves)
                print("Computer move: ", best_move[0], best_move[1])
                # Best_Move = Alpha_Beta()
                newBoard.update_Board(best_move[0], best_move[1], GameState.current_player)
                newBoard.print_board(GameState.current_player)
                GameState.Calculate_Score()
                GameState.switch_player()
