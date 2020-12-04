from typing import List
from packages.geneticAlgo.GeneticItem import GeneticItem
from packages.paths.Point import Point
from packages.paths.PathUtils import find_invalid_move, common_points


class PathObstacleItem(GeneticItem[List[Point]]):
    def __init__(self, value, obstacles: List[Point], grid_width: int):
        super().__init__(value)
        self.obstacles = obstacles
        self.grid_width = grid_width

    def fitness(self) -> float:
        common_obstacles = len(common_points(self.value, self.obstacles))
        return 1 / len(self.value) + min(len(self.obstacles) - common_obstacles, 0)

    def invalid_jump_index(self) -> int:
        return find_invalid_move(self.value)
