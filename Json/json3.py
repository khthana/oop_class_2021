import json

prog_dict = {
    "name": "Python",
    "author": "Guido Van Rossum",
    "year": 1990,
    "frameworks": ["Flask", "Django"],
    "libraries": ["Pandas", "Numpy", "Matplotlib", "Requests"]
}

data = json.load(prog_dict)

# Iterating through the json
# list
for i in data['emp_details']:
    print(i)




