from typing import List
import numpy as np
from .GeneticItem import GeneticItem


def should_happen(chance: float) -> bool:
    if chance > 1 or chance < 0:
        raise Exception('Chance for event must be a value between 0 to 1')

    should = np.random.choice([True, False], 1, p=[chance, 1-chance])
    return should[0]


def roulette_wheel(population: List[GeneticItem]) -> (GeneticItem, GeneticItem):
    total_fitness = sum(item.fitness() for item in population)
    probability = [
        (item.fitness() / total_fitness)
        for item in population
    ]

    parents = np.random.choice(population, 2, p=probability, replace=False)
    return tuple(parents)
