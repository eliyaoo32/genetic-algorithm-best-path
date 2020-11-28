import matplotlib.pyplot as plt
import matplotlib.animation as animation
from typing import List
from packages.paths.BestPathAlgorithm import BestPathAlgorithm
from packages.paths.Point import Point


current_history = 0
def animated_history(history: List[List[Point]]):
    fig = plt.figure()
    ax = plt.axes(xlim=(-1, 11), ylim=(-1, 11))
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line

    def animate(i):
        global current_history

        x = [p.x for p in history[current_history]]
        y = [p.y for p in history[current_history]]

        if current_history + 1 < len(history):
            current_history += 1

        line.set_data(x, y)
        return line

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, interval=100)
    plt.show()


if __name__ == '__main__':
    GRID_WIDTH = 30

    population_size = 120
    max_generation_without_improvement = 10
    small_improvement = 0.0001
    mutation_chance = 0.6

    # start = Point.random(GRID_WIDTH-1)
    # end = Point.random(GRID_WIDTH-1)
    start = Point(0, 0)
    end = Point(10, 10)
    while start == end:
        end = Point.random(GRID_WIDTH-1)

    algo = BestPathAlgorithm(
        mutation_chance, population_size, start, end,
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

    animated_history([item.most_fitted for item in algo.history.all()])
    algo.display_plots()
