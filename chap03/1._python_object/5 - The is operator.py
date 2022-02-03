"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

a = [5, 2, 1, 8, 3]
b = [6, 2, 8, 9, 3]
print(a is b)

a = [5, 2, 1, 8, 3]
b = a
print(a is b)

c = ("a", "b", "c")
d = ("e", "f")
print(c is d)

e = "Hello, World!"
f = "Hello, World!"

print(e is f)
print(f is e)

i = 1000
j = 1000
print(i is j)


