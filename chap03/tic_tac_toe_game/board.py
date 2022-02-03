from move import *
from player import *


class Board:

    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]

    def print_board(self):
        print("\nPositions")
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

        print("Board: ")
        for row in self.game_board:
            print("|", end="")
            for col in row:
                if col == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {col} |", end="")
            print()
        print()

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_col()
        value = self.game_board[row][col]

        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            if player.is_human:
                print("This position is already taken. Please enter another one.")

    def is_game_over(self, player, last_move):
        return((self.check_row(player, last_move))
                or (self.check_col(player, last_move))
                or (self.check_diagonal(player))
                or (self.check_antidiagonal(player)))

    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]

        return board_row.count(player.marker) == 3

    def check_col(self, player, last_move):
        markers_count = 0
        col_index = last_move.get_col()
        for i in range(3):
            if self.game_board[i][col_index] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_diagonal(self, player):
        markers_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_antidiagonal(self, player):
        markers_count = 0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def is_tie(self):
        empty_counter = 0
        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL)

        return empty_counter == 0

    def reset_board(self):
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]

# board = Board()
# player = Player()
# move1 = Slot(2)
# move2 = Slot(5)
# move3 = Slot(8)
#
#
# board.submit_move(player, move1)
# board.submit_move(player, move2)
# board.submit_move(player, move3)
#
# board.print_board()
# print(board.is_game_over(player, move3))
