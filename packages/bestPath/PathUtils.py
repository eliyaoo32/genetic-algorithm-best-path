from typing import List
from .Point import Point
from .utils import rand_item


def generate_path(start: Point, end: Point) -> List[Point]:
    # TODO: make sure it doesn't render an incorrect path
    gen_path: List[Point] = [start]
    head: Point = gen_path[-1]

    while head != end:
        if 'x' == rand_item(['x', 'y']):
            if head.x >= end.x:
                gen_path.append(Point(head.x - 1, head.y))
            else:
                gen_path.append(Point(head.x + 1, head.y))
        else:
            if head.y >= end.y:
                gen_path.append(Point(head.x, head.y - 1))
            else:
                gen_path.append(Point(head.x, head.y + 1))

        head = gen_path[-1]

    return gen_path
