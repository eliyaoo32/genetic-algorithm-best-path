from packages.pathFinder.PathFinderAlgo import PathFinderAlgo
from packages.paths.Point import Point
from packages.animation import animated_history

if __name__ == '__main__':
    MUTATION_CHANCE = 0.2
    POPULATION_SIZE = 80
    TOTAL_GENERATIONS = 100

    start = Point(0, 0)
    end = Point(10, 10)
    algo = PathFinderAlgo(
        mutation_chance=MUTATION_CHANCE,
        population_size=POPULATION_SIZE,
        total_generations=TOTAL_GENERATIONS,
        start=start, end=end
    )
    algo.run()

    algo.display_plots()
    animated_history([item.most_fitted for item in algo.history.all()])
