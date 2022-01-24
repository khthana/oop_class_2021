"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:

    VALID_COLORS = ("Red", "Blue", "Green")

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and radius > 0:
            self._radius = new_radius
        else:
            print("Please enter a valid radius.")

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Please enter a valid color.")

    color = property(get_color, set_color)


my_circle = Circle(10, "Blue")

# Radius
print(my_circle.radius)
my_circle.radius = 16
print(my_circle.radius)

my_circle.radius = 0
print(my_circle.radius)

# Color
print(my_circle.color)
my_circle.color = "Red"
print(my_circle.color)

my_circle.color = "White"
print(my_circle.color)
