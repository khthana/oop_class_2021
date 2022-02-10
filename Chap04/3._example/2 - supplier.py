from contact import Contact


class Supplier(Contact):
    def order(self, order):
        print("Order : ", order)


c = Contact("Some body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
print(c.name, c.email)
print(s.name, s.email)

# c.order("order")
s.order("order")

