class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

class Falcon(Animal):
    category = "birds"

class Parrots(Animal):
    category = "birds"

class Zoo:
    def __init__(self):
            self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()
falcon = Falcon("Falcon")  # create an instance of the Falcon class
parrots = Parrots("Parrots")  # create an instance of the Parrots class
zoo.add_animal(falcon)
zoo.add_animal(parrots)
print(zoo.total_of_category("birds"))  # how many zoo animal types in the birds category

