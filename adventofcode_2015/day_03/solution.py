"""Day 3: Perfectly Spherical Houses in a Vacuum

https://adventofcode.com/2015/day/3

"""
from collections import defaultdict

DIRECTIONS_MAP = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}


def solve(data):
    locations = defaultdict(int)
    current = (0, 0)
    locations[current] = 1

    for ch in data.strip():
        x, y = current
        dx, dy = DIRECTIONS_MAP[ch]
        current = (x + dx, y + dy)
        locations[current] += 1

    return len(locations)


def solve2(data):
    locations_1 = defaultdict(int)
    current_1 = (0, 0)
    locations_1[current_1] = 1

    locations_2 = defaultdict(int)
    current_2 = (0, 0)
    locations_2[current_2] = 1

    for i, ch in enumerate(data.strip()):
        if i % 2 == 0:
            x, y = current_1
            dx, dy = DIRECTIONS_MAP[ch]
            current_1 = (x + dx, y + dy)
            locations_1[current_1] += 1
        else:
            x, y = current_2
            dx, dy = DIRECTIONS_MAP[ch]
            current_2 = (x + dx, y + dy)
            locations_2[current_2] += 1

    common_houses = {}
    common_houses.update(locations_1)
    common_houses.update(locations_2)

    return len(common_houses)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')