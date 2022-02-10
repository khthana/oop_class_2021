class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def resize(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y


class Rectangle(GraphicalEntity):
    pass


class Square(GraphicalEntity):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)

    def resize(self, size):
        super().resize(size, size)


r1 = Rectangle(100, 200, 15, 30)
r2 = Rectangle(150, 280, 23, 55)
q1 = Square(300, 400, 50)


for shape in [r1, r2, q1]:
    size_x = shape.size_x
    size_y = shape.size_y
    shape.resize(size_x*2, size_y*2)


