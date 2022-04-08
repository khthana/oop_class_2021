class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    @property
    def area(self) -> float:
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side: float):
        self.__side = side
        super(Square, self).__init__(side, side)

    @property
    def width(self) -> float:
        return self.__side

    @width.setter
    def width(self, value: float):
        self.__side = value

    @property
    def height(self) -> float:
        return self.__side

    @height.setter
    def height(self, value: float) -> None:
        self.__side = value

r = Rectangle(width=10, height=5)
print(r.area)
# 50
s = Square(side=5)
print(s.area)
# 25
