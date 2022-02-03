import random
from move import *


class Player:
    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, is_human=True):
        self._is_human = is_human

        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def marker(self):
        return self._marker

    @property
    def is_human(self):
        return self._marker == "X"

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        while True:
            user_input = int(input("Please enter your move (1-9) : "))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter integer between 1-9.")
        return move

    def get_computer_move(self):
        random_choice = random.choice(list(range(1, 10)))
        move = Move(random_choice)
        print("Computer move (1-9) : ", move.value)
        return move


# human_player=Player()
# #print(human_player.is_human)
# print(human_player.get_move().value)
#
#
# computer_player = Player(is_human=False)
# print(computer_player.get_move().value)