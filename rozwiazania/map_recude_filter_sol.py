from functools import reduce


# Obliczanie sumy elementów listy za pomocą reduce
def sum_of_list(numbers):
    return reduce(lambda x, y: x + y, numbers)


# Podnoszenie do kwadratu elementów listy za pomocą map
def square_of_list(numbers):
    return list(map(lambda x: x ** 2, numbers))


# Filtrowanie liczb parzystych za pomocą filter
def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


# Złączanie listy napisów w jeden napis za pomocą reduce
def concatenate_strings(strings):
    return reduce(lambda x, y: x + y, strings)


# Konwersja listy napisów na listę ich długości za pomocą map
def string_lengths(strings):
    return list(map(lambda x: len(x), strings))


# Filtrowanie liczb podzielnych przez 3 lub 5 za pomocą filter
def filter_divisible_by_3_or_5(numbers):
    return list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))


# Obliczanie iloczynu elementów listy za pomocą reduce
def product_of_list(numbers):
    return reduce(lambda x, y: x * y, numbers)


# Konwersja listy napisów na listę ich pierwszych liter za pomocą map
def first_letters(strings):
    return list(map(lambda x: x[0], strings))


# Filtrowanie liczb dodatnich za pomocą filter
def filter_positive_numbers(numbers):
    return list(filter(lambda x: x > 0, numbers))


# Obliczanie średniej arytmetycznej listy liczb za pomocą reduce
def average_of_list(numbers):
    return reduce(lambda x, y: x + y, numbers) / len(numbers)


# Przykładowe użycie funkcji
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    strings = ["apple", "banana", "orange"]

    print("Sum of list:", sum_of_list(numbers))
    print("Square of list:", square_of_list(numbers))
    print("Even numbers:", filter_even_numbers(numbers))
    print("Concatenated string:", concatenate_strings(strings))
    print("String lengths:", string_lengths(strings))
    print("Numbers divisible by 3 or 5:", filter_divisible_by_3_or_5(numbers))
    print("Product of list:", product_of_list(numbers))
    print("First letters:", first_letters(strings))
    print("Positive numbers:", filter_positive_numbers(numbers))
    print("Average of list:", average_of_list(numbers))
