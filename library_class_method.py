class Library:
    def __init__(self, books):
        self.books = books

    def display(self):
        print("Total Books:", self.books)


l = Library(500)
l.display()
