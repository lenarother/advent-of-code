"""Day 3: Spiral Memory

https://adventofcode.com/2017/day/3

"""
from itertools import cycle

from santa_helpers.distances import manhattan
from santa_helpers.neighbors import neighbors

LEFT = -1, 0
RIGHT = 1, 0
UP = 0, 1
DOWN = 0, -1


def spiral():
    n, x, y, edge = 0, 0, 0, 0
    directions = cycle([RIGHT, UP, LEFT, DOWN])

    while 1:

        if n == 0:
            yield x, y

        elif edge == 0:
            edge = n // 2 + n % 2
            direction = next(directions)
            dx, dy = direction
            while edge:
                x += dx
                y += dy
                yield x, y
                edge -= 1

        n += 1


def solve(square):
    s = spiral()
    while square:
        position = next(s)
        square -= 1
    return manhattan(position, (0, 0))


def value():
    visited = {}
    for x, y in spiral():
        if (x, y) == (0, 0):
            visited.update({(0, 0): 1})
        else:
            visited.update({
                (x, y):
                sum([visited.get(i, 0) for i in neighbors((x, y), 8)])
            })
        yield visited.get((x, y), None)


def solve2(target):
    for v in value():
        if v > target:
            return v


if __name__ == '__main__':
    result = solve(368078)
    print(f'Example1: {result}')

    result = solve2(368078)
    print(f'Example2: {result}')
