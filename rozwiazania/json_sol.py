import json

# Zadanie 1: Serializacja danych
lista_slownikow = [
    {"imie": "Jan", "nazwisko": "Kowalski", "wiek": 30},
    {"imie": "Anna", "nazwisko": "Nowak", "wiek": 25}
]
with open('dane.json', 'w') as plik:
    json.dump(lista_slownikow, plik)

# Zadanie 2: Deserializacja danych
with open('dane.json', 'r') as plik:
    wczytana_lista = json.load(plik)
print("Zadanie 2:", wczytana_lista)

# Zadanie 3: Aktualizacja danych
nowy_slownik = {"imie": "Adam", "nazwisko": "Mickiewicz", "wiek": 40}
wczytana_lista.append(nowy_slownik)
with open('dane.json', 'w') as plik:
    json.dump(wczytana_lista, plik)

# Zadanie 4: Obsługa różnych typów danych
class PrzykladowaKlasa:
    def __init__(self, nazwa):
        self.nazwa = nazwa

obiekt = PrzykladowaKlasa("Przykład")
# Serializacja niestandardowej klasy
obiekt_serializowany = json.dumps(obiekt.__dict__)
print("Zadanie 4:", obiekt_serializowany)

# Zadanie 5: Konwersja danych z/do innego formatu
# Konwersja listy słowników do formatu JSON
dane = [
    {"imie": "Marcin", "nazwisko": "Nowak", "wiek": 35},
    {"imie": "Monika", "nazwisko": "Kowalska", "wiek": 28}
]
dane_json = json.dumps(dane)

# Konwersja danych z formatu JSON do listy słowników
dane_z_json = json.loads(dane_json)
print("Zadanie 5:", dane_z_json)
