"""Day 14: Regolith Reservoir

https://adventofcode.com/2022/day/14

"""
import re

COORD_RE = re.compile(r'(\d+),(\d+)')


def add_points(scan, current_x, current_y, next_x, next_y):
    if current_y == next_y:
        min_x, max_x = sorted([current_x, next_x])
        for dx in range(min_x, max_x + 1):
            scan.add((dx, next_y))

    elif current_x == next_x:
        min_y, max_y = sorted([current_y, next_y])
        for dy in range(min_y, max_y + 1):
            scan.add((next_x, dy))


def parse_scan(data):
    scan = set()
    for line in data.strip().split('\n'):
        current_x = None
        current_y = None
        for x, y in COORD_RE.findall(line):
            x = int(x)
            y = int(y)
            if current_x and current_y:
                add_points(scan, current_x, current_y, x, y)
            current_x = x
            current_y = y
    return scan


def find_floor(scan):
    return max([y for _, y in scan]) + 2


def add_floor(scan):
    y = find_floor(scan)
    for x in range(-1000, 1000):
        scan.add((x, y))


def sand_drop(scan):
    n = 0
    x = 500
    y = 0
    while True:
        if (500, 0) in scan or y > 200:
            yield n
            return
        if (x, y + 1) not in scan:
            y += 1
        elif (x - 1, y + 1) not in scan:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in scan:
            x += 1
            y += 1
        else:
            scan.add((x, y))
            n += 1
            x = 500
            y = 0
            yield n


def solve(data):
    scan = parse_scan(data)
    return list(i for i in sand_drop(scan))[-1]


def solve2(data):
    scan = parse_scan(data)
    add_floor(scan)
    return list(i for i in sand_drop(scan))[-1]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
