class Product:
    discount = 20

    def get_discount(self):
        return Product.discount

class InHouseProduct(Product):
    def get_discount(self):
        return self.apply_extra_discount()

    def apply_extra_discount(self):
        return self.discount * 1.5

product1 = Product()
product2 = InHouseProduct()

lst = [product1, product2]
for i in lst:
    print(i.get_discount())

