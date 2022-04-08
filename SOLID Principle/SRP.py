class Square:

    def __init__(self, side):
        self.__side = side

    def calculate_area(self):
        return self.__side * 2

    def calculate_perimeter(self):
        return self.__side * 4

    def draw(self): # render image on display
        pass

    def rotate(self):
        pass

class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name

    def save(self):
        pass    # save student to mysql DB

    def get_student(self, student_id):
        return __student_id

    def get_name(self, name):
        return __name


class Employee:

    def save(self): # save to MySQL
        pass

    def calculate_tax(self): # full_time, contract
        pass

    def get_employee_no(self):
        pass

    def set_employee_no(self):
        pass

    def get_employee_name(self):
        pass

    def set_employee_name(self):
        pass

