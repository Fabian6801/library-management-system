from library import Library

def main():
    lib = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Search by ID")
        print("3. Search by Title")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Display All Books")
        print("7. Exit")
        choice = input("Enter choice (1-7): ")

        if choice == "1":
            bid = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            lib.add_book(bid, title, author)

        elif choice == "2":
            bid = input("Enter Book ID to search: ").strip()
            book = lib.find_by_id(bid)
            print(book if book else "Book not found!")

        elif choice == "3":
            title = input("Enter Title to search: ").strip()
            results = lib.find_by_title(title)
            if results:
                for b in results: print(b)
            else:
                print("Book not found!")

        elif choice == "4":
            bid = input("Enter Book ID to borrow: ").strip()
            lib.borrow_book(bid)

        elif choice == "5":
            bid = input("Enter Book ID to return: ").strip()
            lib.return_book(bid)

        elif choice == "6":
            lib.display_books()

        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try 1-7.")

if __name__ == "__main__":
    main()