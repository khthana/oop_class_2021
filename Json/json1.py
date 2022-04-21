import json

test_dict = {
    "name": "Python",
    "author": "Guido Van Rossum",
    "year": 1990,
    "frameworks": ["Flask", "Django"],
    "libraries": ["Pandas", "Numpy", "Matplotlib", "Requests"]
}

print(type(test_dict))
j_string = json.dumps(test_dict)
print(j_string)
print(type(j_string))

