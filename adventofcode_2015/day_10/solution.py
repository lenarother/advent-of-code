"""Day 10: Elves Look, Elves Say

https://adventofcode.com/2015/day/10

"""
from itertools import groupby


def step(data):
    nums = [
        (len(list(group)), n)
        for n, group
        in groupby(list(data))
    ]

    step_result = ''
    for count, n in nums:
        step_result += f'{count}{n}'

    return step_result


def solve(data, steps=40):
    while steps:
        data = step(data)
        steps -= 1
    return len(data)


if __name__ == '__main__':
    input_data = open('input_data.txt').read().strip()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, 50)
    print(f'Example2: {result}')
