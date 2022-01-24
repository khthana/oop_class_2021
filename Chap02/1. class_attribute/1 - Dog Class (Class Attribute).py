"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Dog:
    species = "Canis lupus"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def age_change(self, age):
        self.age = age


jj = Dog("JJ", 10, "Thai")
jj.age = 12
print(jj.age)
