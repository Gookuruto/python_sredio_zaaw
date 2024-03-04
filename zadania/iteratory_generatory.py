'''
Iteratory:
    -Ćwiczenie 1: Sumowanie elementów listy
Stwórz iterator, który będzie sumował elementy z danej listy.

Ćwiczenie 2: Wypisywanie indeksów listy
Stwórz iterator, który będzie wypisywał indeksy elementów danej listy.


Generatory:
Ćwiczenie 1: Generowanie liczb parzystych
Stwórz generator, który będzie generował kolejne liczby parzyste.

Ćwiczenie 2: Generowanie ciągu Fibonacciego
Stwórz generator, który będzie generował kolejne liczby w ciągu Fibonacciego.

'''


#
# # Interator 1
# class ListSumIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = 0
#         self.sum = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.lst):
#             self.sum += self.lst[self.index]
#             self.index += 1
#             return self.sum
#         else:
#             raise StopIteration
#
#
# numbers = [1, 2, 3, 4, 5]
# iterator = ListSumIterator(numbers)
# suma = sum(iterator)
# print(suma)
# for i in iterator:
#     print(i, end=" ")  # 1,3,6,10,15
#
#
# # iterator 2
#
# class ListIndexIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.lst):
#             temp_index = self.index
#             self.index += 1
#             return temp_index
#         else:
#             raise StopIteration
#
#
# # Użycie iteratora
# letters = ['a', 'b', 'c', 'd', 'e']
# iterator = ListIndexIterator(letters)
# for index in iterator:
#     print(index, end=" ")  # Output: 0 1 2 3 4


# Generatory 1:

def even_numbers_generator():
    current = 0
    while True:
        yield current
        current += 2


# Użycie generatora
generator = even_numbers_generator()
for _ in range(5):
    print(next(generator), end=" ")  # Output: 0 2 4 6 8


# Genaratory 2:

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Użycie generatora
generator = fibonacci_generator()
for _ in range(10):
    print(next(generator), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34


fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
print()
print(fib(9))
