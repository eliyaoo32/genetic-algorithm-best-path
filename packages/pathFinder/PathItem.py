from typing import List
from packages.geneticAlgo.GeneticItem import GeneticItem
from packages.paths.Point import Point
from packages.paths.PathUtils import find_invalid_move


class PathItem(GeneticItem[List[Point]]):
    def fitness(self) -> float:
        return 1 / len(self.value)

    def invalid_jump_index(self) -> int:
        return find_invalid_move(self.value)
