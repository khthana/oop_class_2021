class Student:
    def __init__(self, first_name, last_name, weight, height):
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight
        self.height = height
        
    def __str__(self):
        return "{} W: {}kg.({:.1f}lbs) H: {}cm.({:.1f}in)".format(self.first_name, self.weight, self.kg_to_pound(self.weight), self.height, Student.cm_to_inch(self.height))

    @staticmethod
    def kg_to_pound(kg):
        return kg * 2.20462

    @staticmethod
    def cm_to_inch(cm):
        return cm * .393701

s = Student("Fah", "Sairoong", 50, 165)
print(Student.kg_to_pound(50))

