"""Day 15: Beacon Exclusion Zone

https://adventofcode.com/2022/day/15

"""
import re
PATTERN = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')


def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def find_positions(p1, p2, row):
    x1, y1 = p1  # Sensor
    x2, y2 = p2   # Bacon
    dist = manhattan(p1, p2)
    for dy in range(y1 - dist, y1 + dist + 1):
        if dy != row:
            continue
        for dx in range(x1 - dist, x1 + dist + 1):
            p = (dx, dy)
            if manhattan(p1, p) <= dist:
                yield p


def sensor_bacon(data):
    for x1, y1, x2, y2 in PATTERN.findall(data):
        yield (int(x1), int(y1)), (int(x2), int(y2))


def solve(data, row):
    result = set()
    for p1, p2 in sensor_bacon(data):
        for p in find_positions(p1, p2, row):
            result.add(p)
    return len(result) - 1


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 2000000)
    print(f'Example1: {result}')
