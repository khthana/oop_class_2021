class Property:
    def __init__(self, square_meter='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square meter: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    @staticmethod
    def prompt_init():
        return dict(square_feet=input("Enter the square meter: "),
            beds=input("Enter number of bedrooms: "),
            baths=input("Enter number of baths: "))


class Apartment(Property):

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = input("Does the property have a laundry service? (yes/no) : ")
        balcony = input("Does the property have a balcony? (yes/no) : ")
        parent_init.update({"laundry": laundry,"balcony": balcony})
        return parent_init

class House(Property):

    def __init__(self, garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = input("Is the yard fenced? (yes/no) ")
        garage = input("Is there a garage? (yes/no)")
        parent_init.update({"fenced": fenced,"garage": garage})
        return parent_init

