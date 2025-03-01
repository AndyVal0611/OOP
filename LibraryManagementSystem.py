class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f'You have borrowed "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is currently unavailable.')

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f'You have returned "{self.title}".')
        else:
            print(f'"{self.title}" is already available.')

    def __str__(self):
        status = 'Available' if self.is_available else 'Borrowed'
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def display_books(self):
        if not self.books:
            print('No books in the library.')
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

# User interaction loop
while True:
    print('\nMenu:')
    print('1. Display all books')
    print('2. Borrow a book')
    print('3. Return a book')
    print('4. Exit')

    choice = input('Enter your choice (1-4): ')

    if choice == '1':
        print('\nLibrary Collection:')
        library.display_books()
    elif choice == '2':
        title = input('Enter the title of the book to borrow: ')
        book = library.search_book(title)
        if book:
            book.borrow_book()
    elif choice == '3':
        title = input('Enter the title of the book to return: ')
        book = library.search_book(title)
        if book:
            book.return_book()
    elif choice == '4':
        print('Exiting the program. Goodbye!')
        break
    else:
        print('Invalid choice. Please enter a number between 1 and 4.')
