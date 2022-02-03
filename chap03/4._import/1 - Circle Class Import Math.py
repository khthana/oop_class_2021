"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return math.pi * (self.radius ** 2)

