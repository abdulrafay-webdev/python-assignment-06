class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self,name):
        self.name = name
        Book.increment_books()

    @classmethod
    def increment_books(cls):
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")



b1 = Book("Book 1")
b2 = Book("Book 2")
b3 = Book("Book 3")
b4 = Book("Book 4")        
        