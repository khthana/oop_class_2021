class Salary:
    def __init__(self, monthly_income):
        self.monthly_income = monthly_income

    def get_total(self):
        return (self.monthly_income * 12)


class Employee:
    def __init__(self, monthly_income, bonus):
        self.monthly_income = monthly_income
        self.bonus = bonus
        self.obj_salary = Salary(self.monthly_income)

    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus) + ' bath'


obj_emp = Employee(2600, 500)
print(obj_emp.annual_salary())

