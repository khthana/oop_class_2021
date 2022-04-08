def car_behavior(total_speed:float, do_something:str, speed:flaot):
    if do_something == "accelarate":
        total_speed += speed
    elif do_something == "brake":
        total_speed += -speed * 0.2
    print("{}! current speed:".format(do_something),total_speed)
    return true

print(car_behavior(100, "brake", 30))

from abc import ABC, abstractmethod
class CarDoes(ABC):
    @abstractmethod
    def doit(self):
        pass

class CarBr(CarDoes):
    def doit(self,total_speed,speed):
        total_speed += -speed * 0.2
        print("brake! current speed:",total_speed)
        return total_speed

class CarAcc(CarDoes):
    def doit(self,total_speed,speed):
        total_speed += speed
        print("accelerate! current speed:", total_speed)
        return total_speed

def car_behavior(cardoes:CarDoes, total_speed, speed):
    cardoes.doit(total_speed, speed)
    return true

