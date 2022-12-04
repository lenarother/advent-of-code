"""Day 4: Camp Cleanup

https://adventofcode.com/2022/day/4

"""
import re

DATA_RE = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')


def pairs(data):
    for i in DATA_RE.findall(data):
        yield range(int(i[0]), int(i[1]) + 1), range(int(i[2]), int(i[3]) + 1)


def has_full_overlap(r1, r2):
    return set(r1).issubset(r2) or set(r2).issubset(r1)


def has_overlap(r1, r2):
    return bool(set(r1).intersection(r2))


def solve(data, overlap_function=has_full_overlap):
    return sum([overlap_function(r1, r2) for r1, r2 in pairs(data)])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, has_overlap)
    print(f'Example2: {result}')
