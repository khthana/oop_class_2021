"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Polygon:
    
    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color


class Triangle(Polygon):
    pass


my_triangle = Triangle(3, "Blue")

print(my_triangle.num_sides)
print(my_triangle.color)
