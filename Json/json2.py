import json

prog_string = '''
    {
        "name": "Python",
        "author": "Guido Van Rossum",
        "year": 1990,
        "frameworks": ["Flask", "Django"],
        "libraries": ["Pandas", "Numpy", "Matplotlib", "Requests"]
    }'''

print(type(prog_string))
prog_dict = json.loads(prog_string)
print(prog_dict)
print(type(prog_dict))
print(prog_dict["name"])

