from typing import List
from packages.geneticAlgo.GeneticItem import GeneticItem
from packages.bestPath.Point import Point
from packages.bestPath.utils import rand_item


class PathItem(GeneticItem[List[Point]]):
    def fitness(self) -> float:
        return 1 / len(self.value)

    def invalid_jump_index(self) -> int:
        """
        If a point couldn't be arrived from the previous point, it considered a invalid jump
        :return: index of the invalid move | -1 if not found
        """
        for i in range(1, len(self.value)):
            current_item = self.value[i]
            next_item = self.value[i + 1]
            if current_item.distance(next_item) != 1:
                return i

        return -1

    @staticmethod
    def generate_path(start: Point, end: Point):
        # TODO: make sure it doesn't render an incorrect path
        gen_path: List[Point] = [start]
        head: Point = gen_path[-1]

        while head != end:
            if 'x' == rand_item(['x', 'y']):
                if head.x >= end.x:
                    gen_path.append(Point(head.x - 1, head.y))
                else:
                    gen_path.append(Point(head.x + 1, head.y))
            else:
                if head.y >= end.y:
                    gen_path.append(Point(head.x, head.y - 1))
                else:
                    gen_path.append(Point(head.x, head.y + 1))

            head = gen_path[-1]

        return gen_path
