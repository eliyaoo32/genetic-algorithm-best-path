import math
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from .GeneticAlgorithmHistory import GeneticAlgorithmHistory
from .GeneticItem import GeneticItem
from .utils import should_happen

T = TypeVar('T', bound=GeneticItem)


class GeneticAlgorithm(ABC, Generic[T]):
    def __init__(self, mutation_chance: float, population_size: int):
        self.population_size = population_size
        self.mutation_chance = mutation_chance
        self.population: List[T] = self.initial_population()

        # Init history
        self.history = GeneticAlgorithmHistory()
        self.history.add(self.population)

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

    @abstractmethod
    def handle_erroneous(self, item: T) -> T:
        pass

    @abstractmethod
    def is_valid(self, item: T) -> bool:
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
            child = self._merge(parents[0], parents[1])
            if not self.is_valid(child):
                child = self.handle_erroneous(child)

            new_population.append(child)

        self.population = new_population
        self.history.add(self.population)

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

        return self._most_fitted().value

    def display_plots(self):
        # Max fitness graph
        plt.plot([
            x.max_fitness
            for x in self.history.all()
        ], label="Max Fitness")
        plt.plot([
            x.min_fitness
            for x in self.history.all()
        ], label="Min Fitness")
        plt.plot([
            x.average_fitness
            for x in self.history.all()
        ], label="Average Fitness")
        plt.legend()
