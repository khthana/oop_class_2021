"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


print(object)   # Base Class of all Class

print(isinstance(5, object))

print(isinstance([1, 5, 2, 6], object))

print(isinstance((1, 5, 2, 6), object))

print(isinstance("Hello, World!", object))

print(isinstance({"a": 5, "b": 6}, object))

print(isinstance(False, object))

print(isinstance(True, object))

def f(x):
    return x * 2


print(isinstance(f, object))


class Movie:

    def __init__(self, title):
        self.title = title


print(isinstance(Movie, object))
