import csv
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    surname: str
    age: int


# Zadanie 1: Zapisanie danych do pliku CSV
dane = [
    ["Imię", "Nazwisko", "Wiek"],
    ["Jan", "Kowalski", 30],
    ["Anna", "Nowak", 25]
]
with open('dane.csv', 'w', newline='') as plik:
    writer = csv.writer(plik)
    writer.writerows(dane)

# Zadanie 2: Odczyt danych z pliku CSV
wczytane_dane = []
with open('dane.csv', 'r') as plik:
    reader = csv.reader(plik)
    for wiersz in reader:
        wczytane_dane.append(Person(wiersz[0], wiersz[1], wiersz[2]))
print("Zadanie 2:", wczytane_dane)

# Zadanie 3: Aktualizacja danych w pliku CSV
nowy_wiersz = ["Adam", "Mickiewicz", 40]
wczytane_dane.append(nowy_wiersz)
with open('dane.csv', 'w', newline='') as plik:
    writer = csv.writer(plik)
    writer.writerows(wczytane_dane)


# Zadanie 4: Obsługa różnych typów danych
class PrzykladowaKlasa:
    def __init__(self, nazwa):
        self.nazwa = nazwa


obiekt = PrzykladowaKlasa("Przykład")
# Zapis niestandardowej klasy do pliku CSV
with open('klasa.csv', 'w', newline='') as plik:
    writer = csv.writer(plik)
    writer.writerow([obiekt.nazwa])

# Zadanie 5: Konwersja danych z/do innego formatu
# Konwersja danych z pliku tekstowego do formatu CSV
with open('dane_tekstowe.txt', 'r') as plik:
    dane_tekstowe = plik.readlines()
    with open('dane_z_csv.csv', 'w', newline='') as plik_csv:
        writer = csv.writer(plik_csv)
        writer.writerow(dane_tekstowe)

# Konwersja danych z pliku CSV do listy tekstowej
dane_z_csv = []
with open('dane_z_csv.csv', 'r', newline='') as plik_csv:
    reader = csv.reader(plik_csv)
    for wiersz in reader:
        dane_z_csv.extend(wiersz)
print("Zadanie 5:", dane_z_csv)
