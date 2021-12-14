"""Day 7: The Treachery of Whales

https://adventofcode.com/2021/day/7

"""

from collections import Counter

FUEL_COST = {}


def parse(data):
    return Counter(list(map(int, data.strip().split(','))))


def count_fuel(data_dict, position):
    return sum([(abs(k - position) * v) for k, v in data_dict.items()])


def solve(data):
    result = {}
    data = parse(data)
    for position in data:
        result[position] = count_fuel(data, position)
    return min(list(result.values()))


def count_step(current_position, target):
    d = abs(current_position - target)
    if d not in FUEL_COST:
        FUEL_COST[d] = sum(list(range(d+1)))
    return FUEL_COST[d]


def count_fuel2(data_dict, position):
    return sum([(count_step(k, position) * v) for k, v in data_dict.items()])


def solve3(data):
    data = parse(data)
    result = {}
    for x in range(min(data.keys()), max(data.keys()) + 1):
        result[x] = count_fuel2(data, x)
    return min(list(result.values()))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = solve3(input_data)
    print(f'Example2: {result}')
