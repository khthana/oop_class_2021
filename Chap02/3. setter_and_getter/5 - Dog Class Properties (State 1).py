"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Dog:

    def __init__(self, age):
        self.age = age


my_dog = Dog(8)

print(f"My dog is {my_dog.age} years old.")
print("One year later...")

my_dog.age += 1

print(f"My dog is now {my_dog.age} years old.")
