class Professor:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def greet_students(self):
        print("Welcome, dear students")


class ScienceProfessor(Professor):

    def __init__(self, name, age, course):
        Professor.__init__(self, name, age, course)

    def greet_students(self):
        print("Welcome to our Science class, dear students!")

