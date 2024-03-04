'''
Map:

Zwiększ wszystkie liczby z listy numbers o 10.
Zamień wszystkie słowa w liście words na ich długość.
Przekonwertuj wszystkie liczby w liście numbers na napisy.

Reduce:

Przemnóż wszystkie liczby z listy numbers.
Połącz wszystkie słowa z listy words w jedno zdanie.
Znajdź najdłuższy napis z listy words.

Filter:

Wyfiltruj tylko liczby parzyste z listy numbers.
Wyfiltruj tylko słowa z listy words, które zaczynają się od litery "a".
Wyfiltruj tylko słowa z listy words, które mają więcej niż 5 liter.
'''
from typing import Callable, List, Any

numbers = list(range(1, 11))
words = ["apple", "banana", "kiwi", "orange", "grape"]


def convert_number(x):
    return x + 10


result = list(map(lambda x: x + 10, numbers))
expected_value = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(numbers)
print(result)
print(result == expected_value)

# Zamień wszystkie słowa w liście words na ich długość.
len_words = list(map(lambda word: len(word), words))
print(len_words)


def map_custom(funkcja: Callable, kolekcja: List):
    nowa_kolekcja = []
    for element in kolekcja:
        result = funkcja(element)
        nowa_kolekcja.append(result)
    return nowa_kolekcja


def convert_str_to_len(x):
    return len(x)


len_words_custom = map_custom(convert_str_to_len, words)

# import string
#
# print(string.ascii_lowercase)
#
# print(list(map(lambda x: string.ascii_lowercase[x - 1], numbers)))

result = list(map(lambda x: str(x), numbers))
expected_value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(result)

# Filter

result_1 = list(filter(lambda x: x % 2 == 0, numbers))
expected_value_1 = [2, 4, 6, 8, 10]
print(result_1)
result_2 = list(filter(lambda x: x.startswith('a'), words))
expected_value_2 = ["apple"]
print(result_2)
result_3 = list(filter(lambda x: len(x) > 5, words))
expected_value_3 = ["banana", "orange"]
print(result_3)

# Reduce
from functools import reduce

# 1
multiplied = reduce(lambda x, y: x * y, numbers)
print(multiplied)

# 2
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)


# 3
def funckja(x, y):
    if len(x) >= len(y):
        return x
    else:
        return y


max_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(max_word)


def fibbonaci(n):
    initial = (0, 1)
    fib_sequence = reduce(lambda x, y: (x[1], x[0] + x[1]), range(n - 1), initial)
    return fib_sequence[1]

print(fibbonaci(19))
