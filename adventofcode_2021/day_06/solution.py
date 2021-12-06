"""Day 6: Lanternfish

https://adventofcode.com/2021/day/6

"""
from collections import defaultdict
from functools import reduce


def parse(data):
    result = defaultdict(int)
    for n in data.strip().split(','):
        result[int(n)] += 1
    return result


def step(data_dict, _=None):
    new_data = {}
    for n in range(1, 9):
        new_data[n - 1] = data_dict.get(n, 0)
    new_data[6] += data_dict.get(0, 0)
    new_data[8] = data_dict.get(0, 0)
    return new_data


def simulate(data, steps):
    data = parse(data)
    while steps:
        data = step(data)
        steps -= 1
    return data


def solve(data, steps=80):
    data = parse(data)
    data = reduce(step, range(steps), data)
    #result = simulate(data, steps)
    return sum(list(data.values()))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = solve(input_data, steps=256)
    print(f'Example1: {result}')
