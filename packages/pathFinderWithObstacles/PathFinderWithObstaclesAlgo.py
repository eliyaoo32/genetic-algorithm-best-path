from typing import List

from packages.pathFinderWithObstacles.PathObstacleItem import PathObstacleItem
from packages.utils import push_to_list, rand, left_half, right_half
from packages.paths.PathUtils import generate_path_with_obstacles, complete_path, find_invalid_move,\
    find_middle_common_point, has_common_points, common_point_index, generate_path
from packages.paths.Point import Point

from packages.geneticAlgo.GeneticAlgorithm import GeneticAlgorithm
from packages.geneticAlgo.utils import stop_after_n_generations, roulette_wheel


class PathFinderWithObstaclesAlgo(GeneticAlgorithm[PathObstacleItem]):
    def __init__(self, mutation_chance: float, population_size: int,
                 total_generations: int, start: Point, end: Point, obstacles: List[Point],
                 grid_width: int):
        self.total_generations = total_generations
        self.start = start
        self.end = end
        self.obstacles = obstacles
        self.grid_width = grid_width

        super().__init__(mutation_chance, population_size)

    def initial_population(self) -> List[PathObstacleItem]:
        return [
            self._create_path_obstacle_item(generate_path(self.start, self.end))
            for _ in range(self.total_generations)
        ]

    def should_stop(self) -> bool:
        return stop_after_n_generations(self.total_generations, self)

    def mating(self, parent1: PathObstacleItem, parent2: PathObstacleItem) -> PathObstacleItem:
        path1, path2 = parent1.value, parent2.value
        common_point = find_middle_common_point(path1, path2)
        if common_point is None:
            path: List[Point] = left_half(path1) + right_half(path2)
        else:
            i, j = common_point
            path: List[Point] = path1[:i] + path2[j:]

        return self._create_path_obstacle_item(value=path)

    def mutation(self, item: PathObstacleItem) -> PathObstacleItem:
        max_remove_size = min(1, int(len(item.value)*0.3))
        remove_size = rand(1, max_remove_size)
        remove_index = rand(1, len(item.value)-2-remove_size)

        new_path = item.value[0:remove_index] + item.value[remove_index+remove_size:]

        return self._create_path_obstacle_item(value=new_path)

    def select_parents(self) -> (PathObstacleItem, PathObstacleItem):
        return roulette_wheel(self.population)

    def handle_erroneous(self, item: PathObstacleItem) -> PathObstacleItem:
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

        # Fix points which in obstacles
        # point_on_obstacle = common_point_index(path, self.obstacles)
        # while point_on_obstacle != -1:
        #     start = path[point_on_obstacle-1]
        #     if point_on_obstacle+1 >= len(path):
        #         end = self.end
        #     else:
        #         end = path[point_on_obstacle+1]     # Skip the problematic
        #
        #     if start == end:
        #         path.pop(invalid_jump_index)
        #     else:
        #         fixed_path = generate_path_with_obstacles(start, end, self.obstacles)
        #         path = push_to_list(path, point_on_obstacle-1, point_on_obstacle, fixed_path)
        #
        #     point_on_obstacle = common_point_index(path, self.obstacles)

        return self._create_path_obstacle_item(value=path)

    def is_valid(self, item: PathObstacleItem) -> bool:
        start_point = item.value[0]
        end_point = item.value[-1]
        # has_common_with_obstacles = has_common_points(item.value, self.obstacles)

        return (
            item.invalid_jump_index() == -1 and
            end_point == self.end and
            start_point == self.start
        )

    def _create_path_obstacle_item(self, value: List[Point]) -> PathObstacleItem:
        return PathObstacleItem(
            value=value,
            grid_width=self.grid_width,
            obstacles=self.obstacles
        )
