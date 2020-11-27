# Return a random number between star to end (included)
def rand(start, end) -> int:
    raise Exception('rand() not implemented yet')


def rand_item(items):
    raise Exception('rand_item() not implemented yet')


def half(items):
    return items[0:(len(items)//2)]


def push_to_list(array, start, end, pushed_array):
    return array[0:start-1] + pushed_array + array[end:len(array)]
