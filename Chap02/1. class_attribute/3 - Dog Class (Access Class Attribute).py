"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Dog:
    species = "Canis Lupus"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


print(Dog.species)
