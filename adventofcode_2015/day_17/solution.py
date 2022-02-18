"""Day 17: No Such Thing as Too Much

https://adventofcode.com/2015/day/17

"""
from collections import Counter
from itertools import combinations


def parse(data):
    return list(map(int, data.strip().split('\n')))


def find_combinations(containers, target):
    return [
        seq for i in range(len(containers), 0, -1)
        for seq in combinations(containers, i)
        if sum(seq) == target
    ]


def find_combinations_count(containers, target):
    return len(find_combinations(containers, target))


def find_min_combinations_count(containers, target):
    combination_counts = Counter(
        [len(c) for c in find_combinations(containers, target)]
    )
    return combination_counts[min(combination_counts)]


def solve(data, target=150, f=find_combinations_count):
    containers = parse(data)
    return f(containers, target)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, f=find_min_combinations_count)
    print(f'Example1: {result}')
