from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def check_availability(self):
        pass


class Book(Product):
    def calculate_price(self):
        return 10

    def check_availability(self):
        return True


book = Book()
print(book.calculate_price())
print(book.check_availability())
