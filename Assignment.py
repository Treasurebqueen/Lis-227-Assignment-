class Book:
    def __init__(self, title, author):
        self.title = title
        self._author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"Title: {book.title}, Author: {book.author}, Status: {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You've borrowed '{title}'. Enjoy reading!")
                return
        print(f"Sorry, '{title}' is not available for borrowing.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available:
                book.is_available = True
                print(f"Thank you for returning '{title}'.")
                return
        print(f"'{title}' is not a book from this library or it's already returned.")

# Creating books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Creating a library and adding books
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Using the library
library.borrow_book("The Great Gatsby")
library.borrow_book("To Kill a Mockingbird")
library.display_books()
library.return_book("To Kill a Mockingbird")
library.display_books()
