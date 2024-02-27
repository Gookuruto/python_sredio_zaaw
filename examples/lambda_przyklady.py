# dodawanie w lambdzie

add = lambda x, y: x + y


# ekwiwalent notrmalnej funkcji:
def add_v2(x, y):
    return x + y


print(add(3, 5))  # Output: 8

# kwadrat liczby
square = lambda x: x * x
print(square(4))  # Output: 16

# sprawdzanie czy liczba jest parzysta
is_even = lambda x: x % 2 == 0
print(is_even(5))  # Output: False
print(is_even(6))  # Output: True

# Sortowanie listy liczb:
numbers = [4, 2, 7, 1, 9, 3]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)  # Output: [1, 2, 3, 4, 7, 9]

# filtrowanie
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
