class Fruit:
    def __init__(self, name):
        self.name = name

class Weight:
    def __init__(self, kilos):
        self.kilos = kilos

    def __add__(self, otherWeight):
        if type(otherWeight) == int:
            return Weight(self.kilos + otherWeight)
        else:
            return Weight(self.kilos + otherWeight.kilos)

    def __radd__(self, kilos_int):
        return self.__add__(kilos_int)
# This calls __init__ with "Apple" argument:
apple = Fruit("Apple")
print(apple.name) # prints "Apple"

w1 = Weight(50)
w2 = Weight(150)
tot = w1 + w2
print(tot.kilos)

w1 = Weight(50)
total = 150 + w1
print(total.kilos)

w1 = Weight(100)
w2 = Weight(150)
w3 = Weight(220)
total = sum([w1, w2, w3])
print(total.kilos)

