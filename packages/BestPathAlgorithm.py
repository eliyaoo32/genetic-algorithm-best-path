from typing import List

from .Point import Point
from .GeneticAlgorithm import GeneticAlgorithm
from .PathItem import PathItem


class BestPathAlgorithm(GeneticAlgorithm[PathItem]):
    def __init__(self, mutation_chance: float, population_size: int, start: Point, end: Point):
        super().__init__(mutation_chance, population_size)
        self.start = start
        self.end = end

    def initial_population(self) -> List[PathItem]:
        pass

    def should_stop(self) -> bool:
        pass

    def mating(self, parent1: PathItem, parent2: PathItem) -> PathItem:
        pass

    def mutation(self, item: PathItem) -> PathItem:
        pass

    def select_parents(self) -> (PathItem, PathItem):
        pass
