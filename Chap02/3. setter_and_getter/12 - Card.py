
class Card:

    def __init__(self, value):
        self._value = value

    @property
    def get_value(self):
        return self._value

    @get_value.setter
    def set_value(self, new_value):
        if 0 < new_value < 10:
            self._value = new_value
        else:
            print("Please enter a valid value")

