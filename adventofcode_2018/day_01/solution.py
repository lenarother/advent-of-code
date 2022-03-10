"""Day 1: Chronal Calibration

https://adventofcode.com/2018/day/1

"""
import re
from itertools import cycle

NUM_PATTERN = re.compile(r'(\+?-?\d+)\n')


def solve(data):
    return sum(list(map(int, NUM_PATTERN.findall(data))))


def solve2(data):
    nums = cycle((list(map(int, NUM_PATTERN.findall(data)))))
    results = {}
    current_result = 0

    for n in nums:
        current_result += n
        if current_result in results:
            return current_result
        results[current_result] = True


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
