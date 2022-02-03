class Move:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def is_valid(self):
        return 1 <= self._value <= 9

    def get_row(self):
        if self._value in (1, 2, 3):
            return 0    # First row
        elif self._value in (4, 5, 6):
            return 1    # Second row
        else:
            return 2    # Third row

    def get_col(self):
        if self._value in (1, 4, 7):
            return 0    # First col
        elif self._value in (2, 5, 8):
            return 1    # Second col
        else:
            return 2    # Third col


# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9

# slot = Slot(5)
# print(slot.value)
# print(slot.is_valid())
# print(slot.get_row())
# print(slot.get_col())

