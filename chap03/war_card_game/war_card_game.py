"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class WarCardGame:

    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    def start_battle(self, cards_from_war=None):

        print("\n== Let's Start the Battle ==\n")

        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        print(f"Your Card:")
        player_card.show()

        print(f"\nComputer Card: ")
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("\nYou won this round!")
            self.add_cards_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe computer won this round.")
            self.add_cards_to_character(self._computer, cards_won)
        else:
            print("\nIt's a tie. This is war!")
            self.start_war(cards_won)

        return winner

    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_cards_won(self, player_card, computer_card, previous_cards):
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]

    def add_cards_to_character(self, character, list_of_cards):
        for card in list_of_cards:
            character.add_card(card)

    def start_war(self, cards_from_battle):
        player_cards = []
        computer_cards = []

        for i in range(3):
            player_card = self._player.draw_card()
            player_cards.append(player_card)

            computer_card = self._computer.draw_card()
            computer_cards.append(computer_card)

        print("Six hidden cards: XXX XXX")

        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print("Try again. The computer won.")
            return True
        elif self._computer.has_empty_deck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print(f"Excellent. You won, {self._player.name}! Congratulations.")
            return True
        else:
            return False

    def print_stats(self):
        print("\n----")
        print(f"You have {self._player.deck.size} cards on your deck.")
        print(f"The computer has {self._computer.deck.size} cards on its deck.")
        print("----")

    def print_welcome_message(self):
        print("==============================")
        print("|        War Card Game       |")
        print("==============================")
