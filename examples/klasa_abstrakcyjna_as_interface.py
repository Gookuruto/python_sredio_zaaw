from abc import ABC, abstractmethod


# Tworzymy abstrakcje zwierzęcia tzn. robimy klase ktora ma pewnie metody ktore sa w stanie wykonywać wszytskie zwierzęta
from typing import Any


class Animal(ABC):
    # Tworzymy abstrakcyjna metode tj. taka ktora nie ma swoje je implementacji.
    # Za jej implementacje będzie odpowiedzialna klasa dziedzicząca
    @abstractmethod
    def speak(self):
        pass


# Tworzymy konkretną klase zwierzęcia np. Dog
class Dog(Animal):
    # Implementujemy metode speak() poniewaz jest ona wymagana przez klase nadżędną Animal
    def speak(self):
        return "Woof!"


# Tworzymy konkretną klase zwierzęcia Cat
class Cat(Animal):
    # Implementujemy metode speak() poniewaz jest ona wymagana przez klase nadżędną Animal
    def speak(self):
        return "Meow!"


# Stworzmy funkcje ktora nie musi wiedziec o klasach Dog oraz Cat wystarczy, ze wie o klasie Animal
def make_animal_speak(animal: Animal):
    print(animal.speak())


dog = Dog()
cat = Cat()
# Teraz zależnie od tego jakiego typu obiekt podamy do funkcji make_animal_sound otrzymamy różny wynik
make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!
