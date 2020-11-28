from typing import List
import matplotlib.animation as animation
import matplotlib.pyplot as plt
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
