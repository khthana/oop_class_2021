from board import Board
from player import Player


class TicTacToeGame:

    def start(self):
        print("**************************")
        print("  Welcome to Tic-Tac-Toe  ")
        print("**************************")

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()

        while True:     # Game
            while True: # Round
                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.is_tie():
                    print("It's tie. Try again.")
                elif board.is_game_over(player, player_move):
                    print("Awesome. You win!!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.is_game_over(computer, computer_move):
                        print("Sorry. You lose.")
                        break

            play_again = input("Would you like to play again? Enter X for YES or O for NO.")

            if play_again == "O":
                print("Bye!!")
                break
            else:
                self.start_new_round(board)

    def start_new_round(self, board):
        print("**************************")
        print("  Welcome to Tic-Tac-Toe  ")
        print("**************************")
        board.reset_board()
        board.print_board()

game = TicTacToeGame()
game.start()