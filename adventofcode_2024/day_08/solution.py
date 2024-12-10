"""Day 8: Resonant Collinearity

https://adventofcode.com/2024/day/8

"""
from collections import defaultdict
from itertools import combinations


def parse_data(data):
    result = defaultdict(list)
    for y, row in enumerate(data.strip().split('\n')):
        for x, v in enumerate(row.strip()):
            if v != '.':
                result[v].append((x, y))
    return result


def get_next_point(first, second, max_point):
    max_x, max_y = max_point
    x1, y1 = first
    x2, y2 = second
    dx = x1 - x2
    dy = y1 - y2
    new_x = x1 + dx
    new_y = y1 + dy
    if 0 <= new_x <= max_x and 0 <= new_y <= max_y:
        return (new_x, new_y)


def get_anti_locations(first, second, max_point):
    return filter(None, [
        get_next_point(first, second, max_point),
        get_next_point(second, first, max_point)
    ])


def get_anti_locations2(first, second, max_point):
    result = []
    # Extend in one direction
    new_p = first
    other = second
    while new_p:
        result.append(new_p)
        new_other = new_p
        new_p = get_next_point(new_p, other, max_point)
        other = new_other
    # Extend in the other direction
    new_p = second
    other = first
    while new_p:
        result.append(new_p)
        new_other = new_p
        new_p = get_next_point(new_p, other, max_point)
        other = new_other
    return result


def get_max_point(data):
    rows = data.strip().split('\n')
    max_x = len(rows[0]) - 1
    max_y = len(rows) - 1
    return max_x, max_y


def solve(data):
    locations = []
    max_point = get_max_point(data)
    data = parse_data(data)
    for ch in data:
        for pair in combinations(data[ch], 2):
            first, second = pair
            locations.extend(get_anti_locations(first, second, max_point))
    return len(set(locations))


def solve2(data):
    locations = []
    max_point = get_max_point(data)
    data = parse_data(data)
    for ch in data:
        for pair in combinations(data[ch], 2):
            first, second = pair
            locations.extend(get_anti_locations2(first, second, max_point))
    return len(set(locations))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)

    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
