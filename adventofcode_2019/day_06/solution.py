"""Day 6: Universal Orbit Map

https://adventofcode.com/2019/day/6

"""
from collections import defaultdict


def parse_data(data, reverse=False):
    data_dict = defaultdict(set)
    for line in data.strip().split('\n'):
        l, r = line.split(')')
        if reverse:
            data_dict[r].add(l)
        data_dict[l].add(r)
    return data_dict


def solve(data, start='COM'):
    data = parse_data(data)

    distance_sum = 0
    current_distance = 0
    level = [start]
    new_level = []

    while level:
        for child in level:
            new_level += data[child]
            distance_sum += current_distance
        level = new_level
        new_level = []
        current_distance += 1

    return distance_sum


def get_neighbours(positions, visited, data):
    new_positions = set()
    for i in positions:
        if i not in visited:
            new_positions |= set(data[i])
            visited.add(i)
    return new_positions, visited


def solve2(data, start='YOU', target='SAN'):
    data = parse_data(data, reverse=True)

    path_length = 0
    positions = {start}
    visited = set()

    while target not in positions:
        positions, visited = get_neighbours(positions, visited, data)
        path_length += 1

    return path_length - 2


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
    result = solve2(input_data)
    print(f'Example2: {result}')
