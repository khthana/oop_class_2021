"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Dog:

    def __init__(self, age):
        self._age = age

    def get_age(self):
        print("Calling the Getter...")
        return self._age

    def set_age(self, new_age):
        print("Calling the Setter...")
        if isinstance(age, int) and 0 < age < 30:
            self._age = new_age
        else:
            print("Please enter a valid age.")

    age = property(get_age, set_age)


my_dog = Dog(8)
print(f"My dog is {my_dog.age} years old.")
print("One year later...")

my_dog.age += 1
print(f"Now my dog is {my_dog.age} years old.")

