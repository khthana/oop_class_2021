class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y


class ResizableMixin:
    def resize(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y


class ResizableGraphicalEntity(GraphicalEntity, ResizableMixin):
    pass


rge = ResizableGraphicalEntity(5, 4, 200, 300)
rge.resize(1000, 2000)
