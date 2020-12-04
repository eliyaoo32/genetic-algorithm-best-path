from packages.pathFinderWithObstacles.PathFinderWithObstaclesAlgo import PathFinderWithObstaclesAlgo
from packages.paths.PathUtils import generate_points
from packages.animation import animated_history


def get_grid_size() -> int:
    print("Enter the grid width: ")
    return int(input())


def get_total_obstacles() -> int:
    print("How many obstacles? ")
    return int(input())


if __name__ == '__main__':
    grid_width = get_grid_size()
    total_obstacles = get_total_obstacles()

    MUTATION_CHANCE = 0.4
    POPULATION_SIZE = 8 * grid_width
    TOTAL_GENERATIONS = 70

    generated_points = generate_points(total_obstacles + 2, grid_width)
    start = generated_points.pop()
    end = generated_points.pop()
    obstacles = generated_points

    print("Looking for a path from {} to {}, grid width is {}".format(start, end, grid_width))
    print("Obstacles: {}".format(", ".join([str(x) for x in obstacles])))

    algo = PathFinderWithObstaclesAlgo(
        mutation_chance=MUTATION_CHANCE,
        population_size=POPULATION_SIZE,
        total_generations=TOTAL_GENERATIONS,
        start=start, end=end, obstacles=obstacles, grid_width=grid_width
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
        grid_width=grid_width,
        obstacles=obstacles
    )
