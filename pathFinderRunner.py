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
    bestPath = algo.run()

    print("********** INFORMATION **********")
    print("Start Point: {}".format(str(start)))
    print("End Point: {}".format(str(end)))
    print("Total Generations: {}".format(algo.history.total_generations()))
    print("Result:")
    print("1) Path: {}".format("-".join([str(x) for x in bestPath])))
    print("2) Length: {}".format(len(bestPath)))

    algo.display_plots()
    animated_history([item.most_fitted for item in algo.history.all()])

