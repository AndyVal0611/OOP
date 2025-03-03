# Create a class for Book
class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f'\nYou have borrowed "{self.title}".')
        else:
            print(f'\nSorry, "{self.title}" is currently unavailable.')

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f'\nYou have returned "{self.title}".')
        else:
            print(f'\n"{self.title}" is already available.')

    def __str__(self):
        status = 'Available' if self.is_available else 'Borrowed'
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}'

# Create a class for Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print('\nBooks In Library:')
        if not self.books:
            print('No books available in the library.')
        else:
            for book in self.books:
                print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


# Creating Library instance
library = Library()

# Creating and adding books
book1 = Book('Ang Mutya ng Section E', 'Lara Flores', '1234567890')
book2 = Book('The Notebook', 'Nicholas Sparks', '2345678901')
book3 = Book('Emma', 'Jane Austen', '3456789012')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("\nWelcome to AV's Library Management System!")

# User interaction loop
while True:
    print('\nMenu:')
    print('1. Display all books')
    print('2. Borrow a book')
    print('3. Return a book')
    print('4. Exit')

    choice = input('Enter your choice (1-4): ')

    if choice == '1':
        library.display_books()
    elif choice == '2':
        title = input('Enter the title of the book to borrow: ')
        book = library.search_book(title)
        if book:
            book.borrow_book()
            library.display_books()  # Automatically update and show books
        else:
            print('\nBook not found.')
    elif choice == '3':
        title = input('Enter the title of the book to return: ')
        book = library.search_book(title)
        if book:
            book.return_book()
            library.display_books()  # Automatically update and show books
        else:
            print('\nBook not found.')
    elif choice == '4':
        print('Thank you for visiting our library!')
        break
    else:
        print('Invalid choice. Please enter a number between 1 and 4.')