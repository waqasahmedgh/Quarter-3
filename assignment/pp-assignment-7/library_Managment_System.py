import json
from typing import List, Dict, Optional, Union


class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._user_id = user_id
        self._name = name
        self._email = email

    def to_dict(self) -> Dict:
        return {
            'user_id': self._user_id,
            'name': self._name,
            'email': self._email
        }

    @staticmethod
    def from_dict(data: Dict) -> 'User':
        return User(
            user_id=data['user_id'],
            name=data['name'],
            email=data['email']
        )

    def display_info(self) -> None:
        print(f"ID: {self._user_id}, Name: {self._name}, Email: {self._email}")


class Librarian(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)


class Member(User):
    def __init__(self, user_id: int, name: str, email: str, borrowed_books: Optional[List[int]] = None):
        super().__init__(user_id, name, email)
        self._borrowed_books = borrowed_books or []

    def borrow_book(self, book_id: int) -> None:
        self._borrowed_books.append(book_id)

    def return_book(self, book_id: int) -> None:
        self._borrowed_books.remove(book_id)

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data['borrowed_books'] = self._borrowed_books
        return data

    @staticmethod
    def from_dict(data: Dict) -> 'Member':
        return Member(
            user_id=data['user_id'],
            name=data['name'],
            email=data['email'],
            borrowed_books=data.get('borrowed_books', [])
        )

    def display_info(self) -> None:
        super().display_info()
        print(f"Borrowed Books: {self._borrowed_books}")


class Book:
    def __init__(self, book_id: int, title: str, author: str, available: bool = True):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._available = available

    def to_dict(self) -> Dict:
        return {
            'book_id': self._book_id,
            'title': self._title,
            'author': self._author,
            'available': self._available
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        return Book(
            book_id=data['book_id'],
            title=data['title'],
            author=data['author'],
            available=data['available']
        )

    def display_info(self) -> None:
        status = 'Available' if self._available else 'Unavailable'
        print(f"Book ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Status: {status}")

    def borrow(self) -> None:
        if self._available:
            self._available = False
        else:
            print("Book is not available")

    def return_book(self) -> None:
        self._available = True


class LibraryManager:
    def __init__(self, books_file: str, users_file: str):
        self.books_file = books_file
        self.users_file = users_file
        self.books = self._load_books()
        self.users = self._load_users()

    def _load_books(self) -> Dict[int, Book]:
        try:
            with open(self.books_file, 'r') as f:
                data = json.load(f)
            return {book['book_id']: Book.from_dict(book) for book in data}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _load_users(self) -> Dict[int, Union[Librarian, Member]]:
        try:
            with open(self.users_file, 'r') as f:
                data = json.load(f)
            users = {}
            for user in data:
                if user.get('borrowed_books') is not None:
                    users[user['user_id']] = Member.from_dict(user)
                else:
                    users[user['user_id']] = Librarian.from_dict(user)
            return users
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_books(self) -> None:
        with open(self.books_file, 'w') as f:
            json.dump([book.to_dict() for book in self.books.values()], f)

    def _save_users(self) -> None:
        with open(self.users_file, 'w') as f:
            json.dump([user.to_dict() for user in self.users.values()], f)

    def add_book(self, book: Book) -> None:
        if book._book_id in self.books:
            print(f"Book with ID {book._book_id} already exists.")
            return
        self.books[book._book_id] = book
        self._save_books()
        print(f"Book '{book._title}' added successfully.")

    def delete_book(self, book_id: int) -> None:
        if book_id in self.books:
            del self.books[book_id]
            self._save_books()
            print(f"Book with ID {book_id} deleted successfully.")
        else:
            print(f"Book with ID {book_id} not found.")

    def update_book(self, book_id: int, title: Optional[str] = None, author: Optional[str] = None, available: Optional[bool] = None) -> None:
        book = self.books.get(book_id)
        if book:
            if title:
                book._title = title
            if author:
                book._author = author
            if available is not None:
                book._available = available
            self._save_books()
            print(f"Book '{book._title}' updated successfully.")
        else:
            print(f"Book with ID {book_id} not found.")

    def borrow_book(self, user_id: int, book_id: int) -> None:
        user = self.users.get(user_id)
        book = self.books.get(book_id)
        if isinstance(user, Member) and book:
            if book._available:
                book.borrow()
                user.borrow_book(book_id)
                self._save_books()
                self._save_users()
                print(f"Book '{book._title}' borrowed by '{user._name}'.")
            else:
                print(f"Book '{book._title}' is not available.")
        else:
            print("Invalid user or book ID.")

    def return_book(self, user_id: int, book_id: int) -> None:
        user = self.users.get(user_id)
        book = self.books.get(book_id)
        if isinstance(user, Member) and book:
            if book_id in user._borrowed_books:
                book.return_book()
                user.return_book(book_id)
                self._save_books()
                self._save_users()
                print(f"Book '{book._title}' returned by '{user._name}'.")
            else:
                print(f"Book '{book._title}' was not borrowed by '{user._name}'.")
        else:
            print("Invalid user or book ID.")

    def add_user(self, user: Union[Librarian, Member]) -> None:
        if user._user_id in self.users:
            print(f"User with ID {user._user_id} already exists.")
            return
        self.users[user._user_id] = user
        self._save_users()
        print(f"User '{user._name}' added successfully.")

    def delete_user(self, user_id: int) -> None:
        if user_id in self.users:
            del self.users[user_id]
            self._save_users()
            print(f"User with ID {user_id} deleted successfully.")
        else:
            print(f"User with ID {user_id} not found.")

    def list_books(self) -> None:
        if not self.books:
            print("No books available.")
            return
        for book in self.books.values():
            book.display_info()


# Example Usage
if __name__ == "__main__":
    # Initialize the LibraryManager with file paths for books and users
    library_manager = LibraryManager(books_file="books.txt", users_file="users.txt")

    # Librarian adds a book
    librarian = Librarian(1, "Librarian 1", "lib1@example.com")
    library_manager.add_user(librarian)
    book = Book(101, "The Chemistary Book", "Waqas Ahmed Author")
    library_manager.add_book(book)

    # Member borrows a book
    member = Member(2, "Waqas Ahmed", "waqas@example.com")
    library_manager.add_user(member)
    library_manager.borrow_book(user_id=2, book_id=101)

    # Member returns a book
    library_manager.return_book(user_id=2, book_id=101)

    # List all books
    library_manager.list_books()
