"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Backpack:

    def __init__(self):
        self.__items = [] # Two underscores


my_backpack = Backpack()

print(my_backpack.items) # Can't be accessed.

print(my_backpack._items) # Can't be accessed with this name.

print(my_backpack.__items) # Can't be accessed with this name.

print(my_backpack._Backpack__items) # Can be accessed but it shouldn't be.
                                    # It should only be used for special cases.

