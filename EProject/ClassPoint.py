import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

    def length(self, coordinate):
        result = math.sqrt(abs(self.x - coordinate.x) ** 2 + abs(self.y - coordinate.y) ** 2)
        return round(result, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(*args)
        elif type(args[0]) == tuple:
            super().__init__(*args[0])
        else:
            super().__init__(*args)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, other):
        x = self.x + other[0]
        y = self.y + other[1]
        return PatchedPoint(x, y)

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self


def main():
    point = PatchedPoint()
    print(point)
    new_point = point + (2, -3)
    print(point, new_point, point is new_point)


if __name__ == '__main__':
    main()

