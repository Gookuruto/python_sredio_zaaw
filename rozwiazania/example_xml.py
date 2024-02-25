import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

# Tworzenie struktury XML
root = ET.Element("Osoby")

osoba1 = ET.SubElement(root, "Osoba")
imie1 = ET.SubElement(osoba1, "Imie")
imie1.text = "Jan"
nazwisko1 = ET.SubElement(osoba1, "Nazwisko")
nazwisko1.text = "Kowalski"
wiek1 = ET.SubElement(osoba1, "Wiek")
wiek1.text = "30"

osoba2 = ET.SubElement(root, "Osoba")
imie2 = ET.SubElement(osoba2, "Imie")
imie2.text = "Anna"
nazwisko2 = ET.SubElement(osoba2, "Nazwisko")
nazwisko2.text = "Nowak"
wiek2 = ET.SubElement(osoba2, "Wiek")
wiek2.text = "25"

# Tworzenie drzewa XML
tree = ET.ElementTree(root)

# Konwersja drzewa XML do stringa i formatowanie za pomocą xml.dom.minidom
xml_str = ET.tostring(root, encoding="utf-8")
dom = minidom.parseString(xml_str)
formatted_xml = dom.toprettyxml(indent="  ")

# Zapis do pliku XML
with open("osoby.xml", "w") as plik:
    plik.write(formatted_xml)
