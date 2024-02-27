import pickle
import getpass

# Zadanie 1: Serializacja danych
lista_obiektow = [1, 2, 3, 'a', 'b', 'c']
with open('lista_obiektow.pickle', 'wb') as plik:# jezeli otworzymy w mode 'w' to dostaniemy blad przy zapisywaniu
    pickle.dump(lista_obiektow, plik)

# Zadanie 2: Deserializacja danych
with open('lista_obiektow.pickle', 'rb') as plik:# jezeli otworzymy w mode 'r' to dostaniemy blad przy odczycie
    wczytana_lista = pickle.load(plik)
print("Zadanie 2:", wczytana_lista)

# Zadanie 3: Aktualizacja danych
with open('lista_obiektow.pickle', 'rb') as plik:
    lista_obiektow = pickle.load(plik)
nowy_element = 'd'
lista_obiektow.append(nowy_element)
with open('lista_obiektow.pickle', 'wb') as plik:
    pickle.dump(lista_obiektow, plik)

# Zadanie 4: Obsługa różnych typów danych
class PrzykladowaKlasa:
    def __init__(self, nazwa):
        self.nazwa = nazwa

obiekt = PrzykladowaKlasa("Przykład")
with open('obiekt.pickle', 'wb') as plik:
    pickle.dump(obiekt, plik)

with open('obiekt.pickle', 'rb') as plik:
    wczytany_obiekt = pickle.load(plik)
print("Zadanie 4:", wczytany_obiekt.nazwa)
