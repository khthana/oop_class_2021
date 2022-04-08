class BluetoothDevice:
    def connect(self):  # do low level network tasks
        pass
    def scan(self):
        pass

class SmartPhone:
    def __init__(self,tel_no):
        self.__tel_no = tel_no
        self.__bt = BluetoothDevice
        # create object BluetoothDevice in Class

    def connect_bluetooth(self):
        self.__bt.connect()

