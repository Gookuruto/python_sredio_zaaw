from abc import ABC, abstractmethod
from math import pi

print("hello word")


class Figura(ABC):
    @abstractmethod
    def obwod(self):
        pass

    @abstractmethod
    def pole(self):
        pass


class Kwadrat(Figura):
    def pole(self):
        return self.a * self.a

    def obwod(self):
        return self.a * 4

    def __init__(self, a):
        self.a = a


class Trojkat(Figura):
    def pole(self):
        return self.a * self.h / 2

    def obwod(self):
        return self.a + self.b + self.c

    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h


class Kolo(Figura):
    def pole(self):
        return self.r ** 2 * pi

    def obwod(self):
        return self.r * pi * 2

    def __init__(self, r):
        self.r = r


k = Kolo(r=2)
print(k.pole())