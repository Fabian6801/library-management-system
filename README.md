# Library Management System - Day 3 | Nexora 14-Day Challenge

## Description
OOP system to manage books: Add, Search, Borrow, Return, Display.

## How to Run
python main.py
python tests/test_library.py

## Data Structures Explanation
- **List:** `self.books` in Library class stores all Book objects.
- **Objects:** Each Book is an object with attributes `book_id`, `title`, `author`, `is_available`.
- **State Change:** `borrow()` sets `is_available = False`, `return_book()` sets it back to `True`.
- **JSON:** Books saved to `data/books.json` using `to_dict()` / `from_dict()` for persistence.

## Test Cases
1. Add book + duplicate ID rejected
2. Search by ID and Title
3. Borrow available -> success, borrow again -> already borrowed
4. Return borrowed -> success, return again -> not borrowed
5. Borrow missing book -> not found
6. Object state changes correctly