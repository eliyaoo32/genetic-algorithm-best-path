from packages.utils import rand


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def random(end: int) -> 'Point':
        x = rand(0, end)
        y = rand(0, end)
        return Point(x, y)
