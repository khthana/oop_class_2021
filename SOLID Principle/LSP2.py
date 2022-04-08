class Rectangle:
    def __init__(self, width: float = 0, height: float = 0):
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value


class AreaCalculator:
    def calculate(self, rects):
        for r in rects:
            print("Area is : {}".format(r.height * r.width))

class Square(Rectangle):
    def get_width(self) -> float:
        return self._width

    def set_width(self, value: float) -> None:
        self._width = value
        self._height = value

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        self._width = value
        self._height = value

    width = property(get_width, set_width)
    height = property(get_height, set_height)


sq = Square()
sq.width = 8
sq.height = 8

rect = Square()
rect.width = 2
rect.height = 3

liste = [sq, rect]
ac = AreaCalculator()
ac.calculate(liste)
# Area is : 64
# Area is : 9