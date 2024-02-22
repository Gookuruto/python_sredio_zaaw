import math
from typing import List


class A:
    def __init__(self):
        print("From class A")


class B(A):
    def __init__(self):
        A.__init__(self)
        print("From class B")


class C(A):
    def __init__(self):
        A.__init__(self)
        print("From class C")


class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print("From class D")


from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass

    @abstractmethod
    def obwod(self):
        pass


class Kolo(Figura):
    def obwod(self):
        return 2 * math.pi * self._r

    def pole(self):
        return math.pi * self._r ** 2

    def __init__(self, r):
        self._r = r


class Kwadrat(Figura):

    def obwod(self):
        pass

    def pole(self):
        pass


k = Kolo(10)

print(k.pole())
print(k.obwod())


def get_figures() -> List[Figura]:
    lista = [Kolo(3), Kolo(5), Kolo(10), Kwadrat()]
    return lista

















figury = get_figures()

for figura in figury:
    print(figura.obwod())