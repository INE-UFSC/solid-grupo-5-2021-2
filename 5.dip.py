"""
Dependency Inversion Principle
Dependências devem ser feitas sobre abstrações, não sobre implementações concretas
"""
from abc import *


class StatsReporter(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def hp(self):
        pass

    @abstractmethod
    def report(self):
        pass


class Player(StatsReporter):

    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def name(self):
        return self.__name

    def hp(self):
        return self.__hp

    def speed(self):
        return self.__speed

    def report(self):
        print(f'Name:{self.name()}')
        print(f'HP:{self.hp()}')
