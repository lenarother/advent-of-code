"""Day 9: All in a Single Night

https://adventofcode.com/2015/day/9

"""
import itertools
import re

DISTANCE = r'(\w+) to (\w+) = (\d+)'


def parse(data):
    return {
        frozenset([d[0], d[1]]): int(d[2])
        for d in re.findall(DISTANCE, data)
    }


def get_locations(dist_dict):
    locations = list()
    for k in dist_dict:
        locations.extend(list(k))
    return set(locations)


def get_route_distance(route, dist_dict):
    return sum(
        dist_dict[frozenset((l1, l2))]
        for l1, l2 in zip(route[:-1], route[1:])
    )


def distances(locations, dist_dict):
    for route in itertools.permutations(locations):
        yield get_route_distance(route, dist_dict)


def solve(data, func=min):
    dist_dict = parse(data)
    locations = get_locations(dist_dict)
    return func(distances(locations, dist_dict))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, max)
    print(f'Example2: {result}')
