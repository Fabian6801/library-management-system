import json
import os
from book import Book

class Library:
    def __init__(self, filepath="data/books.json"):
        self.filepath = filepath
        self.books = []
        self.load_books()

    def load_books(self):
        if not os.path.exists(self.filepath):
            self.books = []
            return
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(b) for b in data]
        except (json.JSONDecodeError, FileNotFoundError):
            self.books = []

    def save_books(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def add_book(self, book_id, title, author):
        if self.find_by_id(book_id):
            print(f"Error: Book ID {book_id} already exists!")
            return False
        if not title.strip() or not author.strip():
            print("Error: Title and Author cannot be empty!")
            return False
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        self.save_books()
        print(f"Book '{title}' successfully added!")
        return True

    def find_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_by_title(self, title):
        results = []
        for book in self.books:
            if title.lower() in book.title.lower():
                results.append(book)
        return results

    def borrow_book(self, book_id):
        book = self.find_by_id(book_id)
        if not book:
            print("Book not found!")
            return False
        if book.borrow():
            self.save_books()
            print(f"Borrowing successful: '{book.title}'")
            return True
        else:
            print(f"Book '{book.title}' is already borrowed!")
            return False

    def return_book(self, book_id):
        book = self.find_by_id(book_id)
        if not book:
            print("Book not found!")
            return False
        if book.return_book():
            self.save_books()
            print(f"Book '{book.title}' successfully returned!")
            return True
        else:
            print(f"No borrowed book found: '{book.title}' is already available!")
            return False

    def display_books(self):
        if not self.books:
            print("No books in library.")
            return
        print("\n--- All Books ---")
        for book in self.books:
            print(book)