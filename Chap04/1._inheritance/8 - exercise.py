class Mammal:
    def __init__(self, name, age, health, num_offspring, years_in_captivity):
        self.name = name
        self.age = age
        self.health = health
        self.num_offspring = num_offspring
        self.years_in_captivity = years_in_captivity

# Define the Panda class below this line
class Panda(Mammal):
    is_endangered = True

    def __init__(self, name, age, health, num_offspring, years_in_captivity, code):
        Mammal.__init__(self, name, age, health, num_offspring, years_in_captivity)
        self.code = code


my_panda = Panda("Nora", 5, "Good", 2, 5, 24601)