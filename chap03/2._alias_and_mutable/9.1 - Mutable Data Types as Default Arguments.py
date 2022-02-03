class WaitingList:

    def __init__(self, clients=[]):  # The default argument is an empty list
        self.clients = clients

    def add_client(self, client):
        self.clients.append(client)


waiting_list1 = WaitingList()
waiting_list2 = WaitingList()
waiting_list1.add_client("Jake")

print(waiting_list1.clients)
print(waiting_list2.clients)


