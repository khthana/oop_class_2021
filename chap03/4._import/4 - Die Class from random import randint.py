"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

from random import randint


class Die:

    def __init__(self, value):
        self.value = value

    def roll_die(self):
        random_value = randint(1, 6)
        self.value = random_value


my_die = Die(4)

print(my_die.value)
my_die.roll_die()
print(my_die.value)
