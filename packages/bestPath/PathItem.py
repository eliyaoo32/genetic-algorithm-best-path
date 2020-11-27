from typing import List
from packages.geneticAlgo.GeneticItem import GeneticItem
from packages.bestPath.Point import Point


class PathItem(GeneticItem[List[Point]]):
    def fitness(self) -> float:
        return 1 / len(self.value)

    def invalid_jump_index(self) -> int:
        """
        If a point couldn't be arrived from the previous point, it considered a invalid jump
        :return: index of the invalid move | -1 if not found
        """
        for i in range(1, len(self.value)):
            prev_item = self.value[i - 1]
            current_item = self.value[i]

            if current_item.distance(prev_item) != 1:
                return i

        return -1
