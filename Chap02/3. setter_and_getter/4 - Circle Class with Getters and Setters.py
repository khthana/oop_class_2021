"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Please enter a valid value for the radius.")


my_circle = Circle(5.0)
print(my_circle.get_radius())

my_circle.set_radius(0) # This will not change the value.
print(my_circle.get_radius())

my_circle.set_radius("Hello, World!") # This will not change the value.
print(my_circle.get_radius())

my_circle.set_radius(10.5) # This will change the value.
print(my_circle.get_radius())
