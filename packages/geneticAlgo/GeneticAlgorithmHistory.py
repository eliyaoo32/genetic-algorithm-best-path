from typing import List
import math
from dataclasses import dataclass
from .GeneticItem import GeneticItem


@dataclass
class GeneticAlgorithmHistoryItem:
    max_fitness: float
    average_fitness: float
    min_fitness: float


class GeneticAlgorithmHistory:
    def __init__(self):
        self.history: List[GeneticAlgorithmHistoryItem] = []

    def add(self, population: List[GeneticItem]):
        max_fitness: float = -math.inf
        min_fitness: float = math.inf
        total_fitness: float = 0

        for item in population:
            item_fitness = item.fitness()
            if item_fitness > max_fitness:
                max_fitness = item_fitness
            if item_fitness < min_fitness:
                min_fitness = item_fitness
            total_fitness += item_fitness

        avg_fitness = total_fitness / len(population)
        history_item = GeneticAlgorithmHistoryItem(
            max_fitness=max_fitness,
            min_fitness=min_fitness,
            average_fitness=avg_fitness
        )
        self.history.append(history_item)

    def get(self, generation_index: int) -> GeneticAlgorithmHistoryItem:
        return self.history[generation_index]

    def total_generations(self) -> int:
        return len(self.history)

    def last(self, n: int) -> List[GeneticAlgorithmHistoryItem]:
        return self.history[-n:]
