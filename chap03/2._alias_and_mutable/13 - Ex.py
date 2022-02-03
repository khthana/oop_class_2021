a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c


def remove_elem(data, target):  # new_data = data[:]
    for item in data:
        if item == target:
            data.remove(target)
    return data


def get_product(data):
    total = 1
    for i in range(len(data)):
        total *= data.pop()
    return total


remove_elem(c, 3)
print(get_product(b))
print(a)