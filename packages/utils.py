import random
import numpy as np


def rand_item(items):
    return np.random.choice(items)


# Return a random number between star to end (included)
def rand(start, end) -> int:
    return random.randint(start, end)


def remove_same_following_items(array):
    new_array = [array[0]]

    for i in range(1, len(array)):
        item = array[i]
        prev_item = array[i-1]
        if item != prev_item:
            new_array.append(item)

    return new_array


def left_half(items):
    return items[0:(len(items)//2)]


def right_half(items):
    return items[(len(items)//2):]


def get_third(items, index):
    n = len(items)
    return items[int((index-1)*n/3):int(index*n/3)]


def push_to_list(array, start, end, pushed_array):
    return array[0:start] + pushed_array + array[end:len(array)]

