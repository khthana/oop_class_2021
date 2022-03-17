from property import *
from buy_rent import *

class Agent:
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type = get_valid_input("What type of property? ",("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ",("purchase", "rental")).lower()

type_map = { ("house", "rental"): HouseRental,
          ("house", "purchase"): HousePurchase,
          ("apartment", "rental"): ApartmentRental,
          ("apartment", "purchase"): ApartmentPurchase}

PropertyClass = type_map[(property_type, payment_type)]
init_args = PropertyClass.prompt_init()
self.property_list.append(PropertyClass(**init_args))
