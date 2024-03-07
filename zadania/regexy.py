'''
Zadanie: Znajdź wszystkie liczby w tekście.
    Przykładowy tekst: "To jest przykład zdania z liczbą 123 i 456."
    Oczekiwane wyniki: ['123', '456']

Zadanie: Znajdź wszystkie adresy email w tekście.
    Przykładowy tekst: "Kontaktuj się ze mną pod adresem john.doe@example.com lub jane@example.org."
    Oczekiwane wyniki: ['john.doe@example.com', 'jane@example.org']

Zadanie: Znajdź wszystkie daty w formacie DD/MM/RRRR.
    Przykładowy tekst: "Spotkanie odbędzie się 20/02/2023."
    Oczekiwane wyniki: ['20/02/2023']

Zadanie: Znajdź wszystkie słowa zaczynające się wielką literą.
    Przykładowy tekst: "To Jest Przykładowy Tekst Z Kilku Słowami."
    Oczekiwane wyniki: ['To', 'Jest', 'Przykładowy', 'Tekst', 'Z', 'Kilku', 'Słowami']

Zadanie: Znajdź wszystkie linie zaczynające się od słowa "ERROR".
    Przykładowy tekst:
        ERROR: Unable to connect to server.
        WARNING: Disk space is low.
        ERROR: Database connection failed.

    Oczekiwane wyniki:
        ERROR: Unable to connect to server.
        ERROR: Database connection failed.
'''

import re

# 1
import pytest

text = "To jest przykład zdania z liczbą 123 i 456."
pattern = r'[0-9]+'
result = re.findall(pattern, text)
print(result)

# 2

text = "Kontaktuj się ze mną pod adresem john.doe@example.com lub jane@example.org."
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
result = re.findall(pattern, text)
# print(result)

# @pytest.mark.parametrize("email", [
#     "user@example.com",                 # Standardowy adres e-mail
#     "user.name@example.com",            # Adres e-mail z kropką w nazwie użytkownika
#     "user123@example.com",              # Adres e-mail z cyframi w nazwie użytkownika
#     "user.name+tag@example.com",        # Adres e-mail z tagiem
#     "user@example.co.uk",               # Adres e-mail z dwuczęściową domeną
#     # Dodaj więcej przypadków testowych tutaj...
# ])
# def test_email_regex(email):
#     match = re.fullmatch(pattern, email)
#     assert match is not None, f"Failed for email: {email}"

text = "Spotkanie odbędzie się 20/02/2023."

# pattern = r"\b(\d{1,2})\/(\d{2})\/(\d{2}|\d{4})\b"
pattern = r"\d{2}/\d{2}/\d{4}"

print(re.findall(pattern, text))

# find all words started with big letter
text = "To Jest Przykładowy Tekst Z Kilku Słowami."

pattern = r"[A-Z]\w*"

print(re.findall(pattern, text))

'''
Zadanie: Znajdź wszystkie linie zaczynające się od słowa "ERROR".
    Przykładowy tekst:
        ERROR: Unable to connect to server.
        WARNING: Disk space is low.
        ERROR: Database connection failed.

    Oczekiwane wyniki:
        ERROR: Unable to connect to server.
        ERROR: Database connection failed.
'''

text = "ERROR: Unable to connect to server.\n" + "WARNING: Disk space is low.\n" + "ERROR: Database connection failed."
pattern = r"^ERROR.*"

print(text)
result = re.findall(pattern, text, re.MULTILINE)

print(list(result))
