"""Day 14: Regolith Reservoir

https://adventofcode.com/2022/day/14

"""
import re

COORD_RE = re.compile(r'(\d+),(\d+)')


def parse_scan(data):
    scan = {}
    for line in data.strip().split('\n'):
        current_x = None
        current_y = None
        for x, y in COORD_RE.findall(line):
            x = int(x)
            y = int(y)
            if current_x and current_y:
                direction = 'x' if current_y == y else 'y'
                if direction == 'x':
                    min_x, max_x = sorted([current_x, x])
                    for dx in range(min_x, max_x + 1):
                        scan[(dx, y)] = True
                elif direction == 'y':
                    min_y, max_y = sorted([current_y, y])
                    for dy in range(min_y, max_y + 1):
                        scan[(x, dy)] = True
            current_x = x
            current_y = y
    return scan


def find_floor(scan):
    return max([y for _, y in scan]) + 2


def add_floor(scan):
    y = find_floor(scan)
    for x in range(-1000, 1000):
        scan[(x, y)] = True


def sand_drop(scan):
    n = 0
    x = 500
    y = 0
    can_move = True
    while can_move:
        if (500, 0) in scan:
            yield n
            return
        if y == 10000:
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
            scan[(x, y)] = True
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
