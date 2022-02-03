"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    

my_backpack = Backpack()
your_backpack = Backpack()

print(id(my_backpack))

print(id(your_backpack))
