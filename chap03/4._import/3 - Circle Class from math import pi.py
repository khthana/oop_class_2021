"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return pi * (self.radius ** 2)
