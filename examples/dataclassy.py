from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Person:
    imie: str
    nazwisko: str
    wiek: int
    sex: str


class TraditionalDataclassPerson:
    def __init__(self, imie: str, nazwisko: str, wiek: int, sex: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.sex = sex

    def __repr__(self):
        return f"TraditionalDataclassPerson(imie='{self.imie}')"

    def __eq__(self, other):
        return self.imie == other.imie and self.nazwisko == other.nazwisko


class PersonChild(Person):
    def __init__(self):
        super().__init__("a", "b", 1, "m")

    def super_metoda(self):
        print("super")


p = [TraditionalDataclassPerson("Maciej", "Puchała", 50, "M")]
print(p)

print(PersonChild())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


@dataclass
class PointV2:
    x: int
    y: int


print(Point(1, 1) == Point(1, 1))
print(PointV2(1, 1) == PointV2(1, 1))
