"""title

https://adventofcode.com/2023/day/8

"""
import math
import re
from itertools import cycle


def steps_generator(data):
    for i in cycle(data.strip().split("\n")[0]):
        yield i


def parse_instructions(data):
    return {
        key: {'L': left, 'R': right}
        for line in data.strip().split("\n\n")[1].split("\n")
        for key, left, right in re.findall(r'(\w+) = \((\w+), (\w+)\)', line)
    }


def find_number_of_steps(start, is_target, instructions, data):
    current = start
    counter = 0
    for direction in steps_generator(data):
        counter += 1
        current = instructions[current][direction]
        if is_target(current):
            return counter


def solve(data):
    return find_number_of_steps(
        start='AAA',
        is_target=lambda x: x == 'ZZZ',
        instructions=parse_instructions(data),
        data=data,
    )


def solve_2(data):
    instructions = parse_instructions(data)
    starts = filter(lambda x: x.endswith('A'), instructions.keys())
    results = [
        find_number_of_steps(
            start=start,
            is_target=lambda x: x.endswith('Z'),
            instructions=instructions,
            data=data,
        ) for start in starts
    ]
    return math.lcm(*results)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example2: {result}')
