class Car:
    def __init__(self, cabin_width):
        self.cabin_width = cabin_width

    def get_cabin_width(self):
        return cabin_width

class RacingCar(Car):
    def __init__(self, cockpit_width):
        self.cockpit_width = cockpit_width

    def get_cabin_width(self):
        pass # unimplemented

    def get_cockpit_width(self):
        return cockpit_width

car1 = Car(20)
car2 = RacingCar(15)

lst = [car1,car2]
for i in lst:
    print(i.get_cabin_width())



