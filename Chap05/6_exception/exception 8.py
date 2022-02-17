class Backpack:

    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def set_items1(self, new_items):
        if isinstance(new_items, int):
            self._items = new_items
        else:
            print("Please enter a valid list of items.")

    def set_items2(self, new_items):
        try:
            new_items = int(new_items)
        except ValueError:
            return
        self._items = new_items
