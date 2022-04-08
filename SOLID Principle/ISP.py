class ParkingLot:
    def park_car(self):	        # Decrease empty spot count by 1
        raise NotImplementedError

    def unpark_car(self):       # Increase empty spots by 1
        raise NotImplementedError

    def get_capacity(self):     # Returns car capacity
        raise NotImplementedError

    def calculate_fee(self, car): # Returns the price based on number of hours
        raise NotImplementedError

    def do_payment(self, car):
        raise NotImplementedError


class FreeParkingLot(ParkingLot):
    def park_car(self):	        # Decrease empty spot count by 1
        print('parking')

    def unpark_car(self):       # Increase empty spots by 1
        print('unparking')

    def get_capacity(self):     # Returns car capacity
        print('get_capacity')

    def calculate_fee(self, car): # Returns the price based on number of hours
        return 0

    def do_payment(self, car):
        raise Exception("Parking lot is free")


