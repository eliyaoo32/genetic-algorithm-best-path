import matplotlib.pyplot as plt
from typing import List
from packages.bestPath.BestPathAlgorithm import BestPathAlgorithm
from packages.bestPath.Point import Point

if __name__ == '__main__':
    GRID_WIDTH = 20

    max_generation_without_improvement = 10
    small_improvement = 0.00001
    mutation_chance = 0

    # start = Point.random(GRID_WIDTH-1)
    # end = Point.random(GRID_WIDTH-1)
    start = Point(0, 0)
    end = Point(10, 10)
    while start == end:
        end = Point.random(GRID_WIDTH-1)

    algo = BestPathAlgorithm(
        mutation_chance, GRID_WIDTH, start, end,
        max_generation_without_improvement, small_improvement
    )
    bestPath: List[Point] = algo.run()

    print("********** INFORMATION **********")
    print("Start Point: {}".format(str(start)))
    print("End Point: {}".format(str(end)))
    print("Total Generations: {}".format(algo.history.total_generations()))
    print("Result:")
    print("1) Path: {}".format("-".join([str(x) for x in bestPath])))
    print("2) Length: {}".format(len(bestPath)))

    # Max fitness graph
    plt.plot([
        x.max_fitness
        for x in algo.history.all()
    ])
    plt.ylabel('Max fitness')
    plt.xlabel('Generation')
    plt.figure()

    # Min fitness graph
    plt.plot([
        x.min_fitness
        for x in algo.history.all()
    ])
    plt.ylabel('min fitness')
    plt.xlabel('Generation')
    plt.figure()

    # Avg fitness graph
    plt.plot([
        x.average_fitness
        for x in algo.history.all()
    ])
    plt.ylabel('Average fitness')
    plt.xlabel('Generation')
    plt.show()
