"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Movie:
    id_counter = 1

    def __init__(self, title, rating):
        self.id = Movie.id_counter
        self.title = title
        self.rating = rating

        Movie.id_counter += 1


my_movie = Movie("Sense and Sensibility", 4.5)
your_movie = Movie("Legends of the Fall", 4.7)

print(my_movie.id)
print(your_movie.id)
