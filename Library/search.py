from abc import ABC, abstractmethod

class Search(ABC):
  def search_by_title(self, title):
    pass

  def search_by_author(self, author):
    pass

  def search_by_subject(self, subject):
    pass

  def search_by_pub_date(self, publish_date):
    pass

class Catalog(Search):
  def __init__(self):
    self.__book_titles = {}
    self.__book_authors = {}
    self.__book_subjects = {}
    self.__book_publication_dates = {}

  def search_by_title(self, query):
    # return all books containing the string query in their title.
    return self.__book_titles.get(query)

  def search_by_author(self, query):
    # return all books containing the string query in their author's name.
    return self.__book_authors.get(query)
