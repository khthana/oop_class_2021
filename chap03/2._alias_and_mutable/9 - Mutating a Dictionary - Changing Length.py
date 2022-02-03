"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


def remove_even_values(dictionary):
    for key, value in dictionary.items():
        if value % 2 == 0:
            del dictionary[key]


my_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}

remove_even_values(my_dictionary)  # This throws an error.

