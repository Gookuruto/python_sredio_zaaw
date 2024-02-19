from abc import ABC, abstractmethod


class AbstractList(ABC):
    def __init__(self):
        self.data = []

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def contains(self, item):
        pass


class ArrayList(AbstractList):
    def add(self, item):
        self.data.append(item)

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)

    def get(self, index):
        return self.data[index]

    def contains(self, item):
        return item in self.data


lst = ArrayList()
lst.add(1)
lst.add(2)
lst.add(3)
print(lst.get(1))
print(lst.contains(4))
