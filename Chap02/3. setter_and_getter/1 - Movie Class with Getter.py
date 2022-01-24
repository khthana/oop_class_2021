"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Movie:

    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title


my_movie = Movie("The Godfather", 4.8)

print(my_movie.title) # Throws an error

print(my_movie.get_title())
print("My favorite movie is:", my_movie.get_title())
