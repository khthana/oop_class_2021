class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


c = Contact("Some body", "somebody@example.net")
s = Contact("Sup Plier", "supplier@example.net")

print(c.name, c.email)



        