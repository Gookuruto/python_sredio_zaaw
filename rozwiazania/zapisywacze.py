from abc import ABC, abstractmethod
import csv
import json
import pickle
import xml.etree.ElementTree as ET

class ZapisywaczDanych(ABC):
    @abstractmethod
    def zapisz_dane(self, dane, nazwa_pliku):
        pass

class ZapisywaczCSV(ZapisywaczDanych):
    def zapisz_dane(self, dane, nazwa_pliku):
        with open(nazwa_pliku, 'w', newline='') as plik:
            writer = csv.writer(plik)
            writer.writerows(dane)

class ZapisywaczJSON(ZapisywaczDanych):
    def zapisz_dane(self, dane, nazwa_pliku):
        with open(nazwa_pliku, 'w') as plik:
            json.dump(dane, plik)

class ZapisywaczPickle(ZapisywaczDanych):
    def zapisz_dane(self, dane, nazwa_pliku):
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(dane, plik)

class ZapisywaczXML(ZapisywaczDanych):
    def zapisz_dane(self, dane, nazwa_pliku):
        root = ET.Element("Dane")
        for pozycja in dane:
            element = ET.SubElement(root, "Pozycja")
            for klucz, wartosc in pozycja.items():
                pod_element = ET.SubElement(element, klucz)
                pod_element.text = str(wartosc)
        tree = ET.ElementTree(root)
        tree.write(nazwa_pliku)

# Przykładowe użycie:
dane = [
    {"imie": "Jan", "nazwisko": "Kowalski", "wiek": 30},
    {"imie": "Anna", "nazwisko": "Nowak", "wiek": 25}
]

zapisywacz_csv = ZapisywaczCSV()
zapisywacz_csv.zapisz_dane(dane, "dane.csv")

zapisywacz_json = ZapisywaczJSON()
zapisywacz_json.zapisz_dane(dane, "dane.json")

zapisywacz_pickle = ZapisywaczPickle()
zapisywacz_pickle.zapisz_dane(dane, "dane.pickle")

zapisywacz_xml = ZapisywaczXML()
zapisywacz_xml.zapisz_dane(dane, "dane.xml")
