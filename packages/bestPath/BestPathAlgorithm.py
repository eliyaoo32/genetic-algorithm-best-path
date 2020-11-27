from typing import List
from packages.geneticAlgo.GeneticAlgorithm import GeneticAlgorithm
from packages.geneticAlgo.utils import roulette_wheel

from .Point import Point
from .PathItem import PathItem
from .utils import left_half, rand, push_to_list, right_half
from .PathUtils import generate_path


class BestPathAlgorithm(GeneticAlgorithm[PathItem]):
    def __init__(self, mutation_chance: float, grid_width: int,
                 start: Point, end: Point, max_generation_without_improvement, small_improvement):
        self.grid_width = grid_width
        self.start = start
        self.end = end
        self.max_generation_without_improvement = max_generation_without_improvement
        self.small_improvement = small_improvement

        super().__init__(mutation_chance, population_size=grid_width*2)

    def initial_population(self) -> List[PathItem]:
        return [
            PathItem(generate_path(self.start, self.end))
            for i in range(self.population_size)
        ]

    def should_stop(self) -> bool:
        if self.history.total_generations() < self.max_generation_without_improvement:
            return False

        last_history = self.history.last(self.max_generation_without_improvement)
        for i in range(len(last_history)-1):
            max_fit_improvement = abs(last_history[i].max_fitness - last_history[i+1].max_fitness)
            if max_fit_improvement >= self.small_improvement:
                return False

        return True

    def mating(self, parent1: PathItem, parent2: PathItem) -> PathItem:
        path: List[Point] = left_half(parent1.value) + right_half(parent2.value)

        return PathItem(path)

    def mutation(self, item: PathItem) -> PathItem:
        mutation_size = min(1, int(0.05 * self.population_size), len(item.value) // 2)
        start_index = rand(0, len(item.value) - 1 - mutation_size)

        for i in range(mutation_size):
            item.value.pop(start_index+i)

        return item

    def select_parents(self) -> (PathItem, PathItem):
        return roulette_wheel(self.population)

    def handle_erroneous(self, item: PathItem) -> PathItem:
        invalid_jump_index = item.invalid_jump_index()

        while invalid_jump_index != -1:
            start = item.value[invalid_jump_index-1]
            end = item.value[invalid_jump_index]

            if start == end:
                item.value.pop(invalid_jump_index)
            else:
                fixed_path = generate_path(start, end)
                item.value = push_to_list(item.value, invalid_jump_index-1, invalid_jump_index, fixed_path)

            invalid_jump_index = item.invalid_jump_index()

        return item

    def is_valid(self, item: PathItem) -> bool:
        return item.invalid_jump_index() == -1
