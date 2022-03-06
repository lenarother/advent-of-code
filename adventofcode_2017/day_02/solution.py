"""Day 2: Corruption Checksum

https://adventofcode.com/2017/day/2

"""
import itertools
import re


def solve(data):
    results = []
    for row in data.strip().split('\n'):
        nums = list(map(int, re.findall(r'\d+', row)))
        results.append(max(nums) - min(nums))
    return sum(results)


def find_division(row):
    for pair in itertools.combinations(row, 2):
        pair_min = min(pair)
        pair_max = max(pair)
        if pair_max % pair_min == 0:
            return pair_max / pair_min


def solve2(data):
    results = []
    for row in data.strip().split('\n'):
        nums = list(map(int, re.findall(r'\d+', row)))
        results.append(find_division(nums))
    return sum(results)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
