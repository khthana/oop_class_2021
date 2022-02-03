"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Circle:

    def __init__(self, radius):
        self.radius = radius


my_circle = Circle(4)
your_circle = my_circle
print("Before:")
print(my_circle.radius)
print(your_circle.radius)

your_circle.radius = 18
print("After:")
print(my_circle.radius)
print(your_circle.radius)

