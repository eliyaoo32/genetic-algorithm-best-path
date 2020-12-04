from typing import List
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from packages.paths.Point import Point


current_history = 0


def animated_history(history: List[List[Point]], grid_width: int, obstacles=None):
    if obstacles is None:
        obstacles = []
    fig = plt.figure()
    ax = plt.axes(xlim=(-1, grid_width+1), ylim=(-1, grid_width+1))
    line, = ax.plot([], [], lw=2)

    if obstacles:
        ax.plot(
            [p.x for p in obstacles],
            [p.y for p in obstacles],
            'ro'
        )

    def init():
        line.set_data([], [])
        return line

    def animate(_):
        global current_history

        x = [p.x for p in history[current_history]]
        y = [p.y for p in history[current_history]]

        if current_history + 1 < len(history):
            current_history += 1

        line.set_data(x, y)
        return line

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, interval=100)
    plt.show()
