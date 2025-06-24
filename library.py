from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_book_by_id(self, book_id):
        return next((book for book in self.books if book.book_id == book_id), None)

    def list_books(self):
        for book in self.books:
            print(book)
