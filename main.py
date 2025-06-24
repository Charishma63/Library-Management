from library import Library
from book import Book
from user import User

lib = Library()

# Sample data
lib.add_book(Book(1, "1984", "George Orwell"))
lib.add_book(Book(2, "To Kill a Mockingbird", "Harper Lee"))
user1 = User(1, "Alice")
lib.add_user(user1)

while True:
    print("\n1. List Books\n2. Borrow Book\n3. Return Book\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        book_id = int(input("Enter Book ID to borrow: "))
        book = lib.find_book_by_id(book_id)
        if book and user1.borrow_book(book):
            print("Book borrowed.")
        else:
            print("Cannot borrow book.")
    elif choice == '3':
        book_id = int(input("Enter Book ID to return: "))
        book = lib.find_book_by_id(book_id)
        if book and user1.return_book(book):
            print("Book returned.")
        else:
            print("Cannot return book.")
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
