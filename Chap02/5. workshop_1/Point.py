import math


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def move(self, x, y):
        self._x = x
        self._y = x

    def calculate_distance(self, other_point):
        return math.sqrt((self._x - other_point.x) ** 2 + \
                         (self._y - other_point.y) ** 2)


# Test
# point1 = Point(5, 1)
# point2 = Point(8, 10)
# print(point1.calculate_distance(point2))
