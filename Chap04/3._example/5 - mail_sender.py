from contact import Contact


class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)


class MailableContact(Contact, MailSender):
    pass


e = MailableContact("John Smith", "jsmith@example.net")
e.send_mail("Hello, test e-mail.")


