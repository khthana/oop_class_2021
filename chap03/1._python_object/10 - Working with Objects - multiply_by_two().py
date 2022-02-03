my_list = [6, 2, 8, 2]


def multiply_by_two(seq):
    print("Inside the function:", id(my_list))
    for i in range(len(seq)):
        seq[i] *= 2


print("Outside the function:", id(my_list))
multiply_by_two(my_list)

print(my_list)
