from functools import reduce

def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

numbers = [0, 1, 2, 3, 4]
reduce(my_add, numbers)
