from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def start_breaking(self):
        pass
