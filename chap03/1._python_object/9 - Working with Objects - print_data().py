"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

my_list = [6, 2, 8, 2]


def print_data(seq):
    print("Inside the function:", id(seq))
    for elem in seq:
        print(elem)


print("Outside the function:", id(my_list))
print_data(my_list)
