class BookReservation:
  def __init__(self, creation_date, status, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__status = status
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def fetch_reservation_details(self, barcode):
    pass

class BookLending:
  def __init__(self, creation_date, due_date, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__due_date = due_date
    self.__return_date = None
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def lend_book(self, barcode, member_id):
    pass

  def fetch_lending_details(self, barcode):
    pass

class Fine:
  def __init__(self, creation_date, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def collect_fine(self, member_id, days):
    pass

