"""Day 4: High-Entropy Passphrases

https://adventofcode.com/2017/day/4

"""
from collections import Counter


def line_split_simple(line):
    return line.split()


def line_split(line):
    return [''.join(sorted(i)) for i in line.split()]


def solve(data, line_split=line_split_simple):
    return sum(
        set(Counter(line_split(line)).values()) == {1}
        for line in data.strip().split('\n')
    )


def solve2(data):
    return solve(data, line_split)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
