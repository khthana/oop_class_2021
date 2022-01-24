"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Circle:
    radius = 5

    def __init__(self, color):
        self.color = color


print(Circle.radius)

my_circle = Circle("Blue")
your_circle = Circle("Green")

print(my_circle.radius)
print(your_circle.radius)

# Update class attribute
Circle.radius = 10

print(Circle.radius)
print(my_circle.radius)
print(your_circle.radius)
