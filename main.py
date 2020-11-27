from typing import List
from packages.bestPath.BestPathAlgorithm import BestPathAlgorithm
from packages.bestPath.Point import Point

if __name__ == '__main__':
    GRID_WIDTH = 20

    max_generation_without_improvement = 10
    small_improvement = 2
    mutation_chance = 0.1

    start = Point.random(GRID_WIDTH-1)
    end = Point.random(GRID_WIDTH-1)
    while start == end:
        end = Point.random(GRID_WIDTH-1)

    algo = BestPathAlgorithm(
        mutation_chance, GRID_WIDTH, start, end,
        max_generation_without_improvement, small_improvement
    )
    bestPath: List[Point] = algo.run()
    print("-".join([str(x) for x in bestPath]))
