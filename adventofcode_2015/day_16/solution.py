"""Day 16: Aunt Sue

https://adventofcode.com/2015/day/16

"""
import re

AUNT_SUE_PATTERN = re.compile(
    r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')

AUNT_SUE_PROPS = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

AUNT_SUE_GREATER_THAN = ['cats', 'trees']
AUNT_SUE_FEWER_THAN = ['pomeranians', 'goldfish']


def check_property(name, value):
    return AUNT_SUE_PROPS.get(name, None) == int(value)


def check_property_inaccurate(name, value):
    if name in AUNT_SUE_GREATER_THAN:
        return AUNT_SUE_PROPS.get(name, 100) < int(value)
    if name in AUNT_SUE_FEWER_THAN:
        return AUNT_SUE_PROPS.get(name, 0) > int(value)
    return check_property(name, value)


def solve(data, f=check_property):
    for aunt_id, p1, v1, p2, v2, p3, v3 in AUNT_SUE_PATTERN.findall(data):
        if f(p1, v1) and f(p2, v2) and f(p3, v3):
            return aunt_id


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, check_property_inaccurate)
    print(f'Example2: {result}')
