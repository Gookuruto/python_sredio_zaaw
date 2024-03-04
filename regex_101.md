# Wyrażenia regularne (Regex) - Podstawy

## Podstawowe Znaki

- `.`: Dowolny znak, z wyjątkiem nowej linii.
- `[]`: Znak pojedynczy z zestawu.
- `[^]`: Znak spoza zestawu.
- `^`: Początek linii.
- `$`: Koniec linii.
- `*`: Zero lub więcej wystąpień poprzedniego znaku.
- `+`: Jedno lub więcej wystąpień poprzedniego znaku.
- `?`: Zero lub jedno wystąpienie poprzedniego znaku.
- `{n}`: Dokładnie n wystąpień poprzedniego znaku.
- `{n,}`: Co najmniej n wystąpień poprzedniego znaku.
- `{n,m}`: Od n do m wystąpień poprzedniego znaku.

## Klasy Znaków

- `\d`: Dowolna cyfra.
- `\D`: Dowolny znak, który nie jest cyfrą.
- `\w`: Dowolny znak alfanumeryczny.
- `\W`: Dowolny znak, który nie jest alfanumeryczny.
- `\s`: Dowolny biały znak.
- `\S`: Dowolny znak, który nie jest białym znakiem.

## Przykłady w Pythonie

```python
import re

# Sprawdzenie czy ciąg zawiera cyfry
pattern = r'\d+'
text = "To jest rok 2024."
if re.search(pattern, text):
    print("Znaleziono cyfry.")
else:
    print("Nie znaleziono cyfr.")

# Zamiana wszystkich cyfr na 'X'
text = "Mam 3 koty i 2 psy."
new_text = re.sub(r'\d', 'X', text)
print(new_text)  # Output: "Mam X koty i X psy."

# Wyszukiwanie adresów email
text = "Moja poczta to jan.kowalski@example.com, a także anna_nowak@gmail.com."
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)  # Output: ['jan.kowalski@example.com', 'anna_nowak@gmail.com']
