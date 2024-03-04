# # map
# text = "hello world"
# capitalized_text = ''.join(map(lambda x: x.upper(), text))
# print(capitalized_text)  # Output: "HELLO WORLD"

# reduce
from functools import reduce

text = ["h", "e" "l", "l", "o"]
concatenated_text = reduce(lambda x, y: x + y, text)
print(concatenated_text)  # Output: "hello"
# ["he" "l", "l", "o"]
# ["hel","l","o"]
# "hello"

# filter
# text = "hello world"
# filtered_text = ''.join(filter(lambda x: x in 'aeiou', text))
# print(filtered_text)  # Output: "eoo"
#
# lista = [1, 100, 25, 128, 99, 3]
# filtered_lista = list(filter(lambda x: x >= 100, lista))
# print(filtered_lista)
#
#
# def filter_custom(funckja, kolekcja):
#     nowa_kolekcja = []
#     for element in kolekcja:
#         if funckja(element):
#             nowa_kolekcja.append(element)
#     return nowa_kolekcja
#
#
# result = filter_custom(lambda x: x >= 100, lista)

from typing import Any, Callable, List, Optional


def custom_reduce(func: Callable, lst: List[Any]) -> Any:
    # Przypisanie wartości początkowej
    result = lst[0]

    # Iterowanie po pozostałych elementach i wywoływanie funkcji
    for element in lst[1:]:
        result = func(result, element)

    # Zwracamy wynik redukcji
    return result


# Definicja funkcji do zredukowania
def add(x, y):
    return x + y


# Przykładowa lista
numbers = [1, 2, 3, 4, 5]

# Użycie custom_reduce
result = custom_reduce(lambda x, y: x if x == 3 else y, numbers)
print(result)  # Output: 15
