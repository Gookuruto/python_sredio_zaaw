#Wyszukiwanie wzorca w tekście:

import re

text = "Ala ma kota, a kot ma Alę."
pattern = r'\bAla\b'  # Szukamy dokładnie słowo "Ala"

matches = re.findall(pattern, text)
print(matches)  # Output: ['Ala']


# Zamiana wzorca w tekście:

import re

text = "Ala ma kota, a kot ma Alę."
pattern = r'\bAla\b'  # Szukamy dokładnie słowo "Ala"
replacement = "Ola"   # Zamieniamy na "Ola"

new_text = re.sub(pattern, replacement, text)
print(new_text)  # Output: "Ola ma kota, a kot ma Alę."

# Sprawdzenie czy dany ciąg pasuje do wzorca:

import re

text = "Ala ma kota, a kot ma Alę."
pattern = r'\bAla\b'  # Szukamy dokładnie słowo "Ala"

match = re.search(pattern, text)
if match:
    print("Znaleziono dopasowanie!")
else:
    print("Nie znaleziono dopasowania.")
