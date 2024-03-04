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