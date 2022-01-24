"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:

    def __init__(self, radius):
        self.radius = radius

    # Printing the value
    def find_diameter(self):
        print(f"Diameter: {self.radius * 2}")
        # The value could be returned too with:
        # return self.radius * 2
