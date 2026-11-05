import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library import Library
from book import Book

def test_add_and_duplicate():
    lib = Library(filepath="data/test_books.json")
    lib.books = []
    assert lib.add_book("B001", "Python Basics", "John") == True
    assert lib.add_book("B001", "Python Basics", "John") == False
    print("PASS: Add + Duplicate rejected")

def test_search():
    lib = Library(filepath="data/test_books.json")
    lib.books = [Book("B001", "Python Basics", "John"), Book("B002", "Java Guide", "Mary")]
    assert lib.find_by_id("B001").title == "Python Basics"
    assert lib.find_by_id("B999") is None
    assert len(lib.find_by_title("python")) == 1
    print("PASS: Search by ID + Title")

def test_borrow_return():
    lib = Library(filepath="data/test_books.json")
    lib.books = [Book("B001", "Python Basics", "John")]
    assert lib.borrow_book("B001") == True
    assert lib.borrow_book("B001") == False  # Already borrowed
    assert lib.return_book("B001") == True
    assert lib.return_book("B001") == False  # Already available
    print("PASS: Borrow + Return logic")

def test_borrow_missing():
    lib = Library(filepath="data/test_books.json")
    lib.books = []
    assert lib.borrow_book("B999") == False
    assert lib.return_book("B999") == False
    print("PASS: Borrow/Return missing book")

def test_book_state():
    b = Book("B001", "Test", "Author")
    assert b.is_available == True
    b.borrow()
    assert b.is_available == False
    b.return_book()
    assert b.is_available == True
    print("PASS: Object State Changes")

def test_display():
    lib = Library(filepath="data/test_books.json")
    lib.books = [Book("B001", "Python", "John")]
    lib.display_books()
    print("PASS: Display")

if __name__ == "__main__":
    test_add_and_duplicate()
    test_search()
    test_borrow_return()
    test_borrow_missing()
    test_book_state()
    test_display()
    print("\nAll 6 tests passed!")
    # cleanup test file
    if os.path.exists("data/test_books.json"):
        os.remove("data/test_books.json")