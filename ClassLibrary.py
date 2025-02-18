class Book:
    def __init__(self, title, author, year_published, status="Available"):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.status = status

    # Borrow the book if it's available
    def borrow_book(self):
        if self.status == "Available":
            self.status = "Borrowed"
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is not available or is already borrowed.")

    # Return the book if it's borrowed
    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' is already available.")

    # Display the book's information
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year Published: {self.year_published}, Status: {self.status}")

# Initialize Book objects
book1 = Book("Ang Mutya ng Section E", "Lara Flores", 2025)
book2 = Book("The Notebook", "Nicholas Sparks", 1996)
book3 = Book("Emma", "Jane Austen", 1815)

books = [book1, book2, book3]

# Display all books with their status
def display_all_books():
    print("\nAvailable books:")
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. {book.title} by {book.author} ({book.year_published}) - Status: {book.status}")

# Get the book index from user input
def borrow_or_return_book(action):
    try:
        book_index = int(input("\nEnter the number of the book: ")) - 1
        if 0 <= book_index < len(books):
            selected_book = books[book_index]
            if action == "borrow":
                selected_book.borrow_book()
            elif action == "return":
                selected_book.return_book()
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop for user interaction
while True:
    print("Menu:")
    print("1. Display all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            display_all_books()
        elif choice == 2:
            display_all_books()
            borrow_or_return_book("borrow")
        elif choice == 3:
            display_all_books()
            borrow_or_return_book("return")
        elif choice == 4:
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
    except ValueError:
        print("Please enter a valid number.")