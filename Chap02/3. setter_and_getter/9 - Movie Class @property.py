"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        print("Calling the getter...")
        return self._rating
    
    @rating.setter
    def rating(self, new_rating):
        print("Calling the setter...")
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Please enter a valid rating.")


favorite_movie = Movie("Titanic", 4.3)
print(favorite_movie.rating)

favorite_movie.rating = 4.5
print(favorite_movie.rating)

favorite_movie.rating = -5.6 # Invalid value.
print(favorite_movie.rating)
