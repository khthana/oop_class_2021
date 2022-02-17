class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def stock_by_material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count

class Shirt(Clothing):
    material = "Cotton"

class Pants(Clothing):
    material = "Cotton"

formal = Shirt("Formal")
dress_pants = Pants("Dress pants")
formal.add_item(formal.name, formal.material, 13)
dress_pants.add_item(dress_pants.name, dress_pants.material, 7)
polo = Clothing("Cotton")
current_stock = polo.stock_by_material("Cotton")
print(current_stock)