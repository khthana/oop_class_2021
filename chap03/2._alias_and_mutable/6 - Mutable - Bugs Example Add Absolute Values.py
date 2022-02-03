"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


def add_absolute_values(seq):
    for i in range(len(seq)):
        seq[i] = abs(seq[i])
    return sum(seq)


values = [-5, -6, -7, -8]
print("Values Before:", values)

result = add_absolute_values(values)

print("Values After:", values)
