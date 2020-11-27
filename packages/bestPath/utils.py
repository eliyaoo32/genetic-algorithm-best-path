import random
import numpy as np


def rand_item(items):
    return np.random.choice(items)


# Return a random number between star to end (included)
def rand(start, end) -> int:
    return random.randint(start, end)


def half(items):
    return items[0:(len(items)//2)]


def push_to_list(array, start, end, pushed_array):
    return array[0:min(start-1, 0)] + pushed_array + array[end:len(array)]

