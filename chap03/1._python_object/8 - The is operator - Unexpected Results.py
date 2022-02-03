"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

a = 5
b = 5

print(a is b)

a = 257
b = 257

print(a is b)

a = 15000
b = 15000

print(a is b)


a = "H"
b = "H"

print(a is b)


a = "Hi"
print(id(a))

b = "Hi"
print(id(b))

c = "Hi"
print(id(c))

d = "Hi"
print(id(d))

print(a is b is c is d)
