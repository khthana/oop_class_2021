class Personal:
    def __init__(self, name, surname, programming_language, experience):
        self.name = name
        self.surname = surname
        self.programming_language = programming_language
        self.experience = experience
        self.address = None

    def view(self):
        print(f"Personal name & surname: {self.name} {self.surname}")
        print(f"Experience period: {self.experience} year")
        print()
        if self.address:
            print("Address: ")
            print(self.address)
        print()
        print("Programming Languages Used: ")
        data_type = type(self.programming_language)
        if data_type is str:
            print("  - ", self.programming_language)
        elif data_type is tuple or list:
            for language in self.programming_language:
                print("  - ", language)
        else:
            print("Error!")
        print("")
        print("-------------------------")
        print("")

class Address:
    def __init__(self, ad, district, city, land):
        self.ad = ad
        self.district = district
        self.city = city
        self.land = land

    def __str__(self):
        details = [self.ad]
        if self.land:
            details.append(self.land)
            details.append(f"{self.district}/{self.city}")
        return '\n'.join(details)

personal1 = Personal("Markus", "Faber", ("Python", "PHP", "Javascript", "Java"), 18)
personal1.address = Address('Brienner St. 0123', 'Maxvorstadt', 'Munich', "GERMANY")
personal2 = Personal("Arim", "Khandakar", ("NodeJS", "ReactJS"), 6)
personal2.address = Address('Rd No 456', 'Kalachandpur', 'DHAKA', "BANGLADESH")
personal3 = Personal("Julia", "Gage", ("Javascript", "CSS"), 4)
personal1.view()
personal2.view()
personal3.view()