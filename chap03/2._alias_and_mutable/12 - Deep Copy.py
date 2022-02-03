import copy

a = ([5, 2, 6, 2], "Welcome", 67)
b = copy.deepcopy(a)
b[0][0] = -1

print(a)
print(b)







