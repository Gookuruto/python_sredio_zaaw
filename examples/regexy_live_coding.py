'''Znajdź słowo "hello" na początku łańcucha znaków.'''
import re

text = "hello world"

result = re.match(r"hello", text)

if result:
    print("Znaleziono 'hello' na początku łańcucha.")
else:
    print("Nie znaleziono 'hello' na początku łańcucha.")

'''Znajdź pierwsze wystąpienie słowa "world" w tekście.'''
text = "hello world"
result = re.search(r"world", text)
print(result)
if result:
    print("Znaleziono 'world' w tekście.")
else:
    print("Nie znaleziono 'world' w tekście.")

'''Sprawdź, czy łańcuch znaków jest dokładnym dopasowaniem do wzorca.'''

pattern = r'\d+'
text1 = "123"
text2 = "123abc"

result1 = re.fullmatch(pattern, text1)
result2 = re.fullmatch(pattern, text2)

if result1:
    print("Dopasowanie pełne dla", text1)
else:
    print("Brak dopasowania pełnego dla", text1)

if result2:
    print("Dopasowanie pełne dla", text2)
else:
    print("Brak dopasowania pełnego dla", text2)

'''Znajdź wszystkie liczby całkowite w tekście.'''

text = "Ala ma 2 koty i 3 psy."
pattern = r"[0-9]+"
numbers = re.findall(pattern,text)
print("Liczby znalezione w tekście:", numbers)

'''Znajdź wszystkie słowa zaczynające się na literę "a" lub "A" w tekście.'''

text = "Ala ma kota i psa. Adam ma jabłka."
pattern = r'\b[aA][a-z]+\b'
matches = re.finditer(pattern,text)
for match in matches:
    print("Znaleziono:", match.group())
