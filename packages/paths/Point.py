from packages.utils import rand


class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def distance(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    @staticmethod
    def random(end: int) -> 'Point':
        x = rand(0, end)
        y = rand(0, end)
        return Point(x, y)
