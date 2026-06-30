class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(self.title)
        print(self.author)

b = Book("Python Basics", "John")
b.display()
