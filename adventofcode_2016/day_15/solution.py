"""Day 15: Timing is Everything

https://adventofcode.com/2016/day/15

"""
import re

DISC = r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).'


def disc_generator(data):
    for n, positions, start_position in re.findall(DISC, data):
        yield int(n), int(positions), int(start_position)


def is_open(n, positions, start_position, t):
    current_position = start_position + n + t
    return abs(positions - current_position) % positions == 0


def check_time(data, t):
    return all([
        is_open(n, positions, start_position, t)
        for n, positions, start_position in disc_generator(data)
    ])


def solve(data):
    t = 0
    while True:
        if check_time(data, t):
            return t
        t += 1


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data_2.txt').read()
    result = solve(input_data)
    print(f'Example2: {result}')
