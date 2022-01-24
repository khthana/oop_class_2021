"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Backpack:

    def __init__(self):
        self._items = []


my_backpack = Backpack()

print(my_backpack.items) # Can't be accessed.

print(my_backpack._items) # Can be accessed but it shouldn't be.
