"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year


my_car = Car("Porsche", "911 Carrera", 2020)

print(my_car.year) # Can't be accessed

print(my_car._year)
