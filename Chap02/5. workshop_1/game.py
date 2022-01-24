from random import randint
from Point import Point
from Rectangle import Rectangle

rect = Rectangle(Point(randint(0, 9), randint(0, 9)), \
                 Point(randint(10, 19), randint(10, 19)))

print("Rectangle Coordinate : ",
      rect.low_left.x, ",",
      rect.low_left.y, "and",
      rect.up_right.x, ",",
      rect.up_right.y)

user_point = Point(float(input("Guess X : ")),
                   float(input("Guess Y : ")))

print("Your point is inside rectangle :", rect.falls_in_rectangle(user_point))


