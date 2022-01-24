from Point import Point


class Rectangle:
    def __init__(self, low_left, up_right):
        self._low_left = low_left
        self._up_right = up_right

    @property
    def low_left(self):
        return self._low_left

    @property
    def up_right(self):
        return self._up_right

    def falls_in_rectangle(self, point):
        if isinstance(point, Point):
            if self._low_left.x < point.x < self.up_right.x \
                    and self.low_left.y < point.y < self.up_right.y:
                return True
            else:
                return False
        else:
            print("Please provide a valid point")


point1 = Point(5, 1)
point2 = Point(8, 10)
rectangle1 = Rectangle(point1, point2)
rectangle2 = Rectangle(Point(6, 2), Point(10, 12))

print(rectangle1.falls_in_rectangle(Point(6, 15)))

#TODO : ให้แก้โดยเอา method falls_in_rectangle ไปไว้ใน Class Point แทน

#TODO : ให้เขียน method คำนวณพื้นที่สี่เหลี่ยม

