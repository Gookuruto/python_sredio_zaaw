import math

# Generator liczb parzystych
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

# Iterator liczb pierwszych
class PrimeIterator:
    def __init__(self):
        self.num = 2

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if all(self.num % i != 0 for i in range(2, int(math.sqrt(self.num)) + 1)):
                prime = self.num
                self.num += 1
                return prime
            else:
                self.num += 1

# Generator ciągu Fibonacciego
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Iterator filtrujący elementy listy
class FilterIterator:
    def __init__(self, data, condition):
        self.data = data
        self.condition = condition
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            if self.condition(self.data[self.index]):
                result = self.data[self.index]
                self.index += 1
                return result
            else:
                self.index += 1
        raise StopIteration

# Generator nieskończonej sekwencji
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# Iterator mapujący funkcję na elementy listy
class MapIterator:
    def __init__(self, data, func):
        self.data = data
        self.func = func
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.func(self.data[self.index])
            self.index += 1
            return result
        else:
            raise StopIteration

# Przykładowe użycie generatorów i iteratorów
if __name__ == "__main__":
    # Generator liczb parzystych
    even_gen = even_numbers()
    print(next(even_gen))  # Output: 0
    print(next(even_gen))  # Output: 2
    print(next(even_gen))  # Output: 4

    # Iterator liczb pierwszych
    prime_iter = PrimeIterator()
    for _ in range(5):
        print(next(prime_iter))  # Output: 2, 3, 5, 7, 11

    # Generator ciągu Fibonacciego
    fib_gen = fibonacci()
    for _ in range(5):
        print(next(fib_gen))  # Output: 0, 1, 1, 2, 3

    # Iterator filtrujący elementy listy
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filter_iter = FilterIterator(data, lambda x: x % 2 == 0)
    for num in filter_iter:
        print(num)  # Output: 2, 4, 6, 8, 10

    # Generator nieskończonej sekwencji
    inf_seq_gen = infinite_sequence()
    for _ in range(5):
        print(next(inf_seq_gen))  # Output: 0, 1, 2, 3, 4

    # Iterator mapujący funkcję na elementy listy
    data = [1, 2, 3, 4, 5]
    map_iter = MapIterator(data, lambda x: x ** 2)
    for num in map_iter:
        print(num)  # Output: 1, 4, 9, 16, 25
