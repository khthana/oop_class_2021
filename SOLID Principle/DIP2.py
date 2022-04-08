from abc import ABC

class IBluetooth(ABC):
    def connect(self):  # do low level network tasks
        pass
    def scan(self):
        pass

class BluetoothDevice(IBluetooth):
    def connect(self):  # do low level network tasks
        print('bluetooth connect')
    def scan(self):
        print('bluetooth scan')

class SmartPhone:
    def __init__(self,tel_no, bt):
        self.__tel_no = tel_no
        self.__bt = bt

    def connect_bluetooth(self):
        self.__bt.connect()

bt = BluetoothDevice()
phone = SmartPhone('0812345678', bt)







