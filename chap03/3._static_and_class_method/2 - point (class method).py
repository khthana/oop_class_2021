class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @classmethod
    def of(cls, point_string):
        s =  point_string.split("-")
        return cls(int(s[0]),int(s[1]))

p1 = Point(5, 5)
p2 = Point.of("10-10")
print(p2._x)

