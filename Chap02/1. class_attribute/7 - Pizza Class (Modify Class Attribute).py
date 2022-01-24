"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Pizza:

    price = 12.99 # All pizzas will have the same price

    def __init__(self, description, toppings, crust):
        self.description = description
        self.toppings = toppings
        self.crust = crust


print(Pizza.price)

my_pizza = Pizza("Margherita", ["Basil", "Mushrooms"], "New York Style")
print(my_pizza.price)

# Update the class attribute
Pizza.price = 13.99

print(Pizza.price)
print(my_pizza.price)
