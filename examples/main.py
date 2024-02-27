from abc import ABC, abstractmethod
from typing import Callable


class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Orc(Enemy):
    def move(self):
        pass

    def attack(self):
        pass


class Dragon(Enemy):
    def move(self):
        pass

    def attack(self):
        pass


enemies = []
for i in range(10):
    enemies.append(Orc())

for i in range(20):
    enemies.append(Dragon())


def add_enemies(factory: Callable,count):
    for i in range(count):
        enemies.append(factory())

def factory_orc():
    return Orc()