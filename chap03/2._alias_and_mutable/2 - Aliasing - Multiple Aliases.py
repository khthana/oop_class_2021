"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

a = [1, 2, 3, 4]
b = a
c = b
d = c

print(id(a))
print(id(b))
print(id(c))
print(id(d))

print(a is b is c is d)
