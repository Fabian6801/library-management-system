class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True  # True = Available, False = Borrowed

    def borrow(self):
        if not self.is_available:
            return False
        self.is_available = False
        return True

    def return_book(self):
        if self.is_available:
            return False
        self.is_available = True
        return True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_available": self.is_available
        }

    @staticmethod
    def from_dict(data):
        book = Book(data["book_id"], data["title"], data["author"])
        book.is_available = data["is_available"]
        return book