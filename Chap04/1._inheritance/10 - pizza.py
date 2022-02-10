class Pizza:
    def __init__(self, size, toppings, price, rating):
        self.size = size          # "Small", "Medium", or "Large"
        self.toppings = toppings  # A list of toppings
        self.price = price
        self.rating = rating      # Scale from 1 to 5

# Add the subclasses below this line
class PizzaMargherita(Pizza):

    def __init__(self, size, toppings, price, rating, has_extra_cheese):
        Pizza.__init__(self, size, toppings, price, rating)
        self.has_extra_cheese = has_extra_cheese


class PizzaMarinara(Pizza):

    def __init__(self, size, toppings, price, rating, has_extra_basil):
        Pizza.__init__(self, size, toppings, price, rating)
        self.has_extra_basil = has_extra_basil


margherita = PizzaMargherita("small", ["Mushrooms"], 500, 5.0, True)
marinara = PizzaMarinara("Large", ["Basil"], 234, 3.0, False)