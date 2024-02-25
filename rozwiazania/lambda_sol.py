# Sortowanie listy sÅÃ³w wedÅug dÅugoÅci
words = ["apple", "banana", "orange", "kiwi"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# Zliczanie parzystych liczb w liÅcie
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
print(even_count)

# Obliczanie sumy kwadratÃ³w liczb w liÅcie
numbers = [1, 2, 3, 4, 5]
sum_of_squares = sum(map(lambda x: x**2, numbers))
print(sum_of_squares)

# Sprawdzenie, czy wszystkie elementy listy sÄ dodatnie
numbers = [1, 2, 3, -4, 5]
all_positive = all(map(lambda x: x > 0, numbers))
print(all_positive)

# Znalezienie najwiÄkszej liczby w liÅcie
numbers = [5, 8, 2, 10, 3]
max_number = max(numbers, key=lambda x: x)
print(max_number)
