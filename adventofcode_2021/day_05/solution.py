"""Day 5: Hydrothermal Venture

https://adventofcode.com/2021/day/5

"""
import re
from collections import defaultdict

POINTS = r'(\d+),(\d+) -> (\d+),(\d+)'


def parse(points_str):
    x1, y1, x2, y2 = list(map(int, re.findall(POINTS, points_str)[0]))
    return (x1, y1), (x2, y2)


def change_var(v1, v2):
    return v1 if v1 == v2 else v1 + 1 if v1 < v2 else v1 - 1


def get_points(points_str, diagonal=True):
    p1, p2 = parse(points_str)
    x1, y1 = p1
    x2, y2 = p2

    if not diagonal and x1 != x2 and y1 != y2:
        return

    while x1 != x2 or y1 != y2:
        yield x1, y1
        x1 = change_var(x1, x2)
        y1 = change_var(y1, y2)

    yield x2, y2


def solve(data, diagonal=True):
    points = defaultdict(int)

    for line in data.strip().split('\n'):
        for p in get_points(line, diagonal):
            points[p] += 1

    return sum([1 for x in points.values() if x > 1])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, diagonal=False)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = solve(input_data, diagonal=True)
    print(f'Example2: {result}')
