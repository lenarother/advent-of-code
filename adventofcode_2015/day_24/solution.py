"""Day 24: It Hangs in the Balance

https://adventofcode.com/2015/day/24

Product of group 1
Group 1 should contain:
- smallest num packages possible
- smallest product
"""
import itertools
from math import prod


def parse(data):
    return list(map(int, data.strip().split('\n')))


def solve(data, n_groups=3):
    data = parse(data)
    target_weight = sum(data) / n_groups
    if not sum(data) % n_groups == 0:
        return

    for i in range(1, len(data) + 1):
        packages = [
            x for x in set(list(itertools.combinations(data, i)))
            if sum(x) == target_weight
        ]
        if packages:
            return sorted([prod(x) for x in packages])[0]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, 4)
    print(f'Example2: {result}')
