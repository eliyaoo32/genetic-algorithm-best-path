from typing import TypeVar, Generic
from abc import ABC, abstractmethod

G = TypeVar('G')


class GeneticItem(ABC, Generic[G]):
    def __init__(self, item: G):
        self.item = item

    @abstractmethod
    def fitness(self) -> float:
        pass
