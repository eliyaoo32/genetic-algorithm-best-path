from packages.pathFinder.PathFinderAlgo import PathFinderAlgo
from packages.paths.Point import Point
from packages.animation import animated_history


def get_grid_size() -> int:
    print("Enter the grid width: ")
    return int(input())


if __name__ == '__main__':
    grid_width = get_grid_size()

    MUTATION_CHANCE = 0.4
    POPULATION_SIZE = 8 * grid_width
    TOTAL_GENERATIONS = 140

    start = Point.random(grid_width)
    end = Point.random(grid_width)
    while end == start:
        end = Point.random(grid_width)

    print("Looking for a path from {} to {}, grid width is {}".format(start, end, grid_width))

    algo = PathFinderAlgo(
        mutation_chance=MUTATION_CHANCE,
        population_size=POPULATION_SIZE,
        total_generations=TOTAL_GENERATIONS,
        start=start, end=end
    )
    bestPath = algo.run()

    print("********** INFORMATION **********")
    print("Start Point: {}".format(str(start)))
    print("End Point: {}".format(str(end)))
    print("Total Generations: {}".format(algo.history.total_generations()))
    print("Result:")
    print("1) Path: {}".format("-".join([str(x) for x in bestPath])))
    print("2) Length: {}".format(len(bestPath)))

    algo.display_plots()
    animated_history(
        history=[item.most_fitted for item in algo.history.all()],
        grid_width=grid_width
    )
