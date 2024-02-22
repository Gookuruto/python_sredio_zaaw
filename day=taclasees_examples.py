from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int


class BookV2:
    def __init__(self, title: str, author: str, year: int):
        self.author = author
        self.title = title
        self.year = year


b = Book("Wiedzmin", "Spakowski", 1990)

print(b)
