# '''
# sorted(iterable, key=func):
# Sortuje elementy w iterable (np. listy) według określonej func klucza.
# func to funkcja, która zwraca wartość, według której sortujemy elementy.
# Działa na różnych kolekcjach, takich jak listy, tuple i inne iterowalne obiekty.
# '''
# # Przykład użycia sorted z funkcją klucza
# words = ["apple", "cherry", "bananana", "durian"]
# sorted_words = sorted(words, key=len)  # Sortuje słowa według ich długości
# # ["apple", "banana", "cherry", "durian"]
# x = [(5, "apple"), (8, "bananana"), (6, "cherry"), (6, "durian")]
# x = [(5, "apple"), (6, "cherry"), (6, "durian"), (8, "bananana")]
# x = [item[1] for item in x]
# print(x)
# print(sorted_words)  # Output: ['apple', 'banana', 'cherry', 'durian']
#
# '''
# max(iterable, key=func):
# Znajduje maksymalną wartość w iterable, według określonego func klucza.
# func to funkcja, która zwraca wartość, według której porównujemy elementy.
# '''
#
# # Przykład użycia max z funkcją klucza
# numbers = [5, 10, 2, 8, 3]
# max_num = max(numbers, key=lambda x: x % 3)  # Znajduje maksymalną liczbę modulo 3
# input = [5, 10, 2, 8, 3]
# x = [2, 1, 2, 2, 0]
# output = input[3]
# print(output)
# print(max_num)  # Output: 5
#
# '''
# min(iterable, key=func):
# Znajduje minimalną wartość w iterable, według określonego func klucza.
# func to funkcja, która zwraca wartość, według której porównujemy elementy.
# '''
#
# # Przykład użycia min z funkcją klucza
# numbers = [5, 10, 2, 8, 3]
# min_num = min(numbers, key=lambda x: abs(x - 7))  # Znajduje najbliższą wartość do 7
# x = [2, 3, 5, 1, 4]
# output = numbers[-2]
# print(output)
# print(min_num)  # Output: 8
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Telefon", "price": 800},
    {"name": "Smartwatch", "price": 300},
    {"name": "Tablet", "price": 1000}
]

min_price_element = min(products, key=lambda x: x["price"])
print(f"Produkt o najniższej cenie: {min_price_element}")

max_price_element = max(products, key=lambda x: x["price"])
print(f"Produkt o najwyższej cenie: {max_price_element}")
