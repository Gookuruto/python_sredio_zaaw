from abc import abstractmethod, ABC
from typing import List


class Calculator(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def mul(self):
        pass

    @abstractmethod
    def div(self):
        pass

    def wypisz(self):
        print("Klasa abstrakcyjna")


class ComplexCalculator(Calculator):

    def __init__(self, a_r, a_im, b_r, b_im):
        self.a = complex(a_r, a_im)
        self.b = complex(b_r, b_im)

    def div(self):
        return self.a / self.b

    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def add(self):
        return self.a + self.b


class NormalCalculator(Calculator):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div(self):
        return self.a / self.b

    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def add(self):
        return self.a + self.b

    def wypisz(self):
        print(f"{self.a}, {self.b}")


def get_calulators() -> List[Calculator]:
    return [ComplexCalculator(1, 0, 4, 3), NormalCalculator(1, 2), NormalCalculator(1, 1)]
