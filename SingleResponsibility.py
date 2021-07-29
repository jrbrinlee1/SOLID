"""
SOLID Design Principles

Single responsibility Principle: A class should have ONE responsibility and no more

Motivation: Maintainability, testability, flexibility & extensibility, parallel development, loose coupling

Implementation:
"""


class BadBooks:
    """
    Bad because books class is storing books and should not write to disk
    """

    def __init__(self):
        self.books = {}
        self.number = 0

    def add_book(self, book):
        self.number += 1
        self.books[self.number] = book

    def store_books_to_disk(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.books))


class Books:
    """
    Better because books now has one responsibility
    """

    def __init__(self):
        self.books = {}
        self.number = 0

    def add_book(self, book):
        self.number += 1
        self.books[self.number] = book


class StoreBooks:
    @staticmethod
    def store_books_to_disk(filename, books):
        with open(filename, 'w') as f:
            f.write(str(books))
