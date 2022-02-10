"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Polygon:
    
    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color


class Triangle(Polygon):

    NUM_SIDES = 3
    
    def __init__(self, base, height, color):
        super().__init__(Triangle.NUM_SIDES, color)
        self.base = base
        self.height = height


my_triangle = Triangle(5, 4, "blue")

print(my_triangle.num_sides)
print(my_triangle.color)
print(my_triangle.base)
print(my_triangle.height)





