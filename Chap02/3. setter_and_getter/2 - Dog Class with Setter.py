"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Dog:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            print("Please enter a valid name.")

my_dog = Dog("Nora", 8)
print("My dog is:", my_dog.get_name())
my_dog.set_name("Norita")
print("Her new name is:", my_dog.get_name())

