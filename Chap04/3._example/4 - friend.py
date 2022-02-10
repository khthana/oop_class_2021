from contact import Contact


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone =  phone


