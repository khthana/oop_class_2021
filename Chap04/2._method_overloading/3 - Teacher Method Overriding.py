"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Teacher:

    def __init__(self, full_name, teacher_id):
        self.full_name = full_name
        self.teacher_id = teacher_id

    def welcome_students(self):
        print(f"Welcome to class!, I'm your teacher. My name is {self.full_name}")


class ScienceTeacher(Teacher):

    def welcome_students(self):
        print(f"Science is amazing.")
        print(f"Welcome to class. I'm your teacher: {self.full_name}")


my_science_teacher = ScienceTeacher("Emily Smith", "S355A213")
my_science_teacher.welcome_students()
