import example
from zapisywacze_abstact.JSONSaver import JSONSaver
from zapisywacze_abstact.pickle_SAVER import PickleSaver
dane = [
    {"imie": "Jan", "nazwisko": "Kowalski", "wiek": 30},
    {"imie": "Anna", "nazwisko": "Nowak", "wiek": 25}
]
example.save_element(JSONSaver(),dane,"pickle.pickle")

class SubClass:
    def __init__(self):
        self.fajnie = "fajnie"
class SuperKlasa:
    def __init__(self):
        self.name = "name"
        self.cos = 10
        self.kalsa = SubClass()

    def __dict__(self):
        result = {
            "name": self.name,
            "cos": self.cos,
            "kalsa": self.kalsa.__dict__
        }
        return result


print(SuperKlasa().__dict__())