import math
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from .GeneticItem import GeneticItem

T = TypeVar('T', bound=GeneticItem)


def should_happen(chance: float) -> bool:
    raise Exception('should_happen() not implemented yet')


class GeneticAlgorithm(ABC, Generic[T]):
    def __init__(self, mutation_chance: float, population_size: int):
        self.population_size = population_size
        self.mutation_chance = mutation_chance
        self.population: List[T] = self.initial_population()

    @abstractmethod
    def initial_population(self) -> List[T]:
        pass

    @abstractmethod
    def should_stop(self) -> bool:
        pass

    @abstractmethod
    def mating(self, parent1: T, parent2: T) -> T:
        pass

    @abstractmethod
    def mutation(self, item: T) -> T:
        pass

    @abstractmethod
    def select_parents(self) -> (T, T):
        pass

    def _merge(self, parent1: T, parent2: T) -> T:
        item: T = self.mating(parent1, parent2)
        if should_happen(self.mutation_chance):
            item = self.mutation(item)

        return item

    def _new_generation(self):
        new_population: List[T] = []
        for i in range(len(self.population)):
            parents = self.select_parents()
            new_population.append(self._merge(parents[0], parents[1]))

        self.population = new_population

    def _most_fitted(self) -> T:
        fitness = -math.inf
        fitted_item = None

        for item in self.population:
            item_fitness = item.fitness()
            if item_fitness > fitness:
                fitness = item_fitness
                fitted_item = item

        return fitted_item

    def run(self):
        while not self.should_stop():
            self._new_generation()

        return self._most_fitted().item
