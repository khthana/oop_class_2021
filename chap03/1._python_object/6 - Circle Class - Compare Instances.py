"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:

    def __init__(self, radius):
        self.radius = radius

my_circle = Circle(5)
your_circle = Circle(10)

print(my_circle is your_circle)

print(my_circle == your_circle)