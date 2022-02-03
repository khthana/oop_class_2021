"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

a = [7, 3, 2, 1]
a[0] = 5
print(a)

a = (7, 3, 2, 1)
a[0] = 5 # This throws an error because tuples are immutable.

a = "Hello, World!"
a[0] = "S" # This throws an error because strings are immutable.
