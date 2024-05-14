# Controller.py

from OthelloBoard import OthelloBoard
from OthelloState import OthelloGameState


class Game:
    def StartGame(self):
        newBoard = OthelloBoard()
        GameState = OthelloGameState(newBoard)

        BlackDisks,WhiteDisks = 30,30
        counter = 0

        print("Game Start\n")
        # Choose difficulty level
        print("Choose difficulty level: \nEasy--> 1 \nMedium--> 2\nHard--> 3\n")
        level = int(input("Enter level: "))
        # check if level is not valid
        if level != 1 and level != 2 and level != 3:
            while True:
                print("Invalid level")
                print("Choose difficulty level: \nEasy--> 1 \nMedium--> 2\nHard--> 3\n")
                level = int(input("Enter level: "))
                if level == 1 or level == 2 or level == 3:
                    break

        # Controller
        while newBoard.has_empty_places():

            if GameState.human_turn:
                if WhiteDisks == 0 or BlackDisks == 0:
                    print("no more disks")
                    if WhiteDisks == 0:
                        print(" For AI")
                    else:
                        print(" For Player")
                    break
                possible_moves = GameState.Possible_Moves_User()
                # when no available move for current player
                if not possible_moves and newBoard.has_white_nodes() and counter == 0:
                    print("No possible moves for player ", GameState.current_player)
                    GameState.switch_player()
                    counter += 1
                    continue
                # when no available move for both player and computer
                elif counter > 0:
                    print("Game Over")
                    BScore, WScore = GameState.Calculate_Score()
                    print("Player: ", BScore)
                    print("Computer: ", WScore)
                    print("Winner is: ")
                    if BScore > WScore:
                        print("Player")
                    elif WScore > BScore:
                        print("Computer")
                    else:
                        print("Draw")
                    break

                newBoard.show_possible_moves(possible_moves, GameState.current_player)
                row = int(input("Enter row: "))
                col = int(input("Enter col: "))

                while newBoard.board[row][col] == '_' or (row, col) not in possible_moves or newBoard.board[row][col] != 'X':
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
                    Black ,White =GameState.Calculate_Score()
                    print("Player: ", Black)
                    print("AI: ", White)
                    GameState.switch_player()
                    newBoard.print_board(GameState.current_player)
                    counter = 0
                    BlackDisks -= 1

            else:
                # Computer Turn
                #check if there is no possible moves for computer
                if not GameState.Possible_Moves_Computer(GameState.board) and newBoard.has_black_nodes() and counter == 0 :
                    print("No possible moves for player ", GameState.current_player)
                    GameState.switch_player()
                    counter += 1
                    continue

                testBoard = OthelloBoard()
                testBoard.board = [['_' for j in range(8)] for i in range(8)]

                if level == 1:
                    best_move = GameState.alpha_beta_Purned(True, testBoard, 1, -1000, 1000, True)

                elif level == 2:
                    best_move = GameState.alpha_beta_Purned(True, testBoard, 2, -1000, 1000, True)

                elif level == 3:
                    best_move = GameState.alpha_beta_Purned(True, testBoard, 3, -1000, 1000, True)

                if best_move[0] == -10000:
                    print("No possible moves for player ", GameState.current_player)
                    GameState.switch_player()
                    counter += 1
                    continue
                newBoard.update_Board(best_move[1][0], best_move[1][1], GameState.current_player)
                newBoard.print_board(GameState.current_player)
                Black, White = GameState.Calculate_Score()
                print("Player: ", Black)
                print("AI: ", White)
                GameState.switch_player()
                counter =0
                WhiteDisks -= 1

        print("Game End\n")
        print("Final Result: \n")
        BScore, WScore = GameState.Calculate_Score()
        print("Player: ", BScore)
        print("AI: ", WScore)
        print("Winner is: ")
        if BScore > WScore:
            print("Player")
        elif WScore > BScore:
            print("AI")

# if len(possible_moves) == 0:
                #     print("Game Over")
                #     GameState.switch_player()
                #     break
                # row, col = choice(possible_moves)
                # print("Computer move: ", best_move[0], best_move[1])
                # Best_Move = Alpha_Beta()

