class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def show(self):
        print("Movie:", self.name)
        print("Rating:", self.rating)


m = Movie("Interstellar", 9.5)
m.show()
