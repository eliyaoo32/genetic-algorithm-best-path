from typing import List

from packages.bestPath.PathItem import PathItem
from packages.bestPath.utils import push_to_list, rand, left_half, right_half, get_third
from packages.bestPath.PathUtils import generate_path, complete_path, find_invalid_move, find_middle_common_point
from packages.bestPath.Point import Point

from packages.geneticAlgo.GeneticAlgorithm import GeneticAlgorithm
from packages.geneticAlgo.utils import stop_after_n_generations, roulette_wheel


class PathFinderAlgo(GeneticAlgorithm[PathItem]):
    def __init__(self, mutation_chance: float, population_size: int,
                 total_generations: int, start: Point, end: Point):
        self.total_generations = total_generations
        self.start = start
        self.end = end

        super().__init__(mutation_chance, population_size)

    def initial_population(self) -> List[PathItem]:
        return [
            PathItem(value=generate_path(self.start, self.end))
            for _ in range(self.total_generations)
        ]

    def should_stop(self) -> bool:
        return stop_after_n_generations(self.total_generations, self)

    def mating(self, parent1: PathItem, parent2: PathItem) -> PathItem:
        path1, path2 = parent1.value, parent2.value
        common_point = find_middle_common_point(path1, path2)
        if common_point is None:
            path: List[Point] = left_half(path1) + right_half(path2)
        else:
            i, j = common_point
            path: List[Point] = path1[:i] + path2[j:]

        return PathItem(value=path)

    def mutation(self, item: PathItem) -> PathItem:
        max_remove_size = min(1, int(len(item.value)*0.3))
        remove_size = rand(1, max_remove_size)
        remove_index = rand(1, len(item.value)-2-remove_size)

        new_path = item.value[0:remove_index] + item.value[remove_index+remove_size:]

        return PathItem(value=new_path)

    def select_parents(self) -> (PathItem, PathItem):
        return roulette_wheel(self.population)

    def handle_erroneous(self, item: PathItem) -> PathItem:
        path: List[Point] = item.value

        # If not the path is not starting or ending in the right points
        if path[0] != self.start:
            path = complete_path(self.start, path[0]) + path[1:]
        if path[-1] != self.end:
            path = path + complete_path(path[-1], self.end)[1:]

        # Invalid jumps
        invalid_jump_index = find_invalid_move(path)
        while invalid_jump_index != -1:
            start = path[invalid_jump_index-1]
            end = path[invalid_jump_index]

            if start == end:
                path.pop(invalid_jump_index)
            else:
                fixed_path = complete_path(start, end)
                path = push_to_list(path, invalid_jump_index-1, invalid_jump_index, fixed_path)

            invalid_jump_index = find_invalid_move(path)

        return PathItem(value=path)

    def is_valid(self, item: PathItem) -> bool:
        start_point = item.value[0]
        end_point = item.value[-1]

        return (
            item.invalid_jump_index() == -1 and
            end_point == self.end and
            start_point == self.start
        )
