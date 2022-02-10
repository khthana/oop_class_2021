"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Backpack:

	def __init__(self):
		self.items = []

	def add_snack(self, snack):
		print("Adding a snack to this backpack...")
		self.items.append(snack)
		print(f"{snack.capitalize()} was added to the backpack successfully.")


class SchoolBackpack(Backpack):

	def add_snack(self, snack):
		print("It's time to go to school. Let's add a snack.")
		Backpack.add_snack(self, snack)
		print("Now you backpack has these items:", self.items)


my_backpack = SchoolBackpack()
my_backpack.add_snack("Candy")
