'''
sorted:

Posortuj listę liczb od najmniejszej do największej.
Posortuj listę słów alfabetycznie.
Posortuj listę liczb od największej do najmniejszej.
Sortowanie listy słów według ostatniej litery:
max:

Znajdź największą liczbę z listy liczb.
Znajdź najdłuższy napis z listy słów.
Znajdź największą liczbę bezwzględną z listy liczb.
min:

Znajdź najmniejszą liczbę z listy liczb.
Znajdź najkrótszy napis z listy słów.
Znajdź najmniejszą liczbę bezwzględną z listy liczb.
'''

# Listy liczb
numbers_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers_2 = [-10, 0, 20, -30, 40, -50]

# Lista słów
words = ["apple", "banana", "kiwi", "orange", "grape"]

# Lista liczb całkowitych i zmiennoprzecinkowych
numbers_float = [3.14, 1.23, 4.56, 0.99, 2.71]

# Lista liczb całkowitych i ujemnych
numbers_negative = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3]

abs(-3)
# min
print(min(numbers_float, key=lambda x: str(x)))
# max
print(max(numbers_float, key=lambda x: str(x)))
# sorted
# sortujemy alfabetycznie po 2 literze
print(sorted(words, key=lambda x: x[1]))

words = ["apple", "banana", "kiwi", "orange", "grape"]

sorted_words = sorted(words, key=lambda x: x[-1])
print(sorted_words)
