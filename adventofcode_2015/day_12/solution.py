"""Day 12: JSAbacusFramework.io

https://adventofcode.com/2015/day/12

"""
import json
import re

NUMBERS = re.compile(r'(-?\d+)')
RED_NUMBERS = re.compile(r'\{.*red.*\d+.*\}')


def solve(data):
    return sum(list(map(int, NUMBERS.findall(data))))


def is_valid_number(v):
    return (
        isinstance(v, str) and
        v.lstrip('-').isnumeric() and
        v.count('-') < 2
    )


def is_valid_dict(v):
    return (
        isinstance(v, dict) and
        'red' not in v.values()
    )


def solve2(data):
    numbers_sum = 0
    data = json.loads(data)
    q = [data]

    while q:
        child = q.pop()
        if isinstance(child, list):
            q.extend(child)
        elif is_valid_dict(child):
            q.extend(list(child.values()))
        elif is_valid_number(child):
            numbers_sum += int(child)
        elif isinstance(child, int):
            numbers_sum += child

    return numbers_sum


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
