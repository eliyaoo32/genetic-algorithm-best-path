from typing import List
from .Point import Point
from packages.utils import rand_item


def is_point_in_list(point: Point, point_list: List[Point]) -> bool:
    return len([p for p in point_list if p == point]) > 0


def common_points(points1: List[Point], points2: List[Point]) -> List[Point]:
    return [
        p
        for p in points1
        if is_point_in_list(p, points2)
    ]


def has_common_points(points1: List[Point], points2: List[Point]) -> bool:
    return len(common_points(points1, points2)) > 0


def common_point_index(path: List[Point], points: List[Point]) -> int:
    for i in range(len(path)):
        point = path[i]
        if is_point_in_list(point, points):
            return i

    return -1


def generate_path(start: Point, end: Point) -> List[Point]:
    gen_path: List[Point] = [start]
    head: Point = gen_path[-1]

    while head != end:
        if 'x' == rand_item(['x', 'y']):
            if head.x >= end.x:
                gen_path.append(Point(max(head.x - 1, 0), head.y))
            else:
                gen_path.append(Point(head.x + 1, head.y))
        else:
            if head.y >= end.y:
                gen_path.append(Point(head.x, max(head.y - 1, 0)))
            else:
                gen_path.append(Point(head.x, head.y + 1))

        head = gen_path[-1]

    return gen_path


def generate_path_with_obstacles(start: Point, end: Point, obstacles: List[Point]) -> List[Point]:
    gen_path: List[Point] = [start]
    head: Point = gen_path[-1]

    while head != end:
        if 'x' == rand_item(['x', 'y']):
            if head.x >= end.x:
                new_point = Point(max(head.x - 1, 0), head.y)
            else:
                new_point = Point(head.x + 1, head.y)
        else:
            if head.y >= end.y:
                new_point = Point(head.x, max(head.y - 1, 0))
            else:
                new_point = Point(head.x, head.y + 1)

        if not is_point_in_list(new_point, obstacles):
            gen_path.append(new_point)

        head = gen_path[-1]

    return gen_path


def complete_path(start: Point, end: Point) -> List[Point]:
    path = [start]
    head = path[-1]

    while head.x != end.x:
        new_x = head.x + 1 if head.x < end.x else head.x-1
        path.append(Point(new_x, head.y))
        head = path[-1]

    while head.y != end.y:
        new_y = head.y + 1 if head.y < end.y else head.y-1
        path.append(Point(head.x, new_y))
        head = path[-1]

    return path


def find_invalid_move(path: List[Point]) -> int:
    """
    If a point couldn't be arrived from the previous point, it considered a invalid jump
    :return: index of the invalid move | -1 if not found
    """
    for i in range(1, len(path)):
        prev_item = path[i - 1]
        current_item = path[i]

        if current_item.distance(prev_item) != 1:
            return i

    return -1


def find_middle_common_point(path1: List[Point], path2: List[Point]):
    for i in range(int(len(path1)/3), int(2/3*len(path1))):
        for j in range(int(len(path2)/3), int(2/3*len(path2))):
            point1 = path1[i]
            point2 = path2[j]
            if point1 == point2:
                return i, j
    return None


def generate_points(total: int, end: int) -> List[Point]:
    points = []
    while len(points) < total:
        new_point = Point.random(end)
        if not is_point_in_list(new_point, points):
            points.append(new_point)
    return points
