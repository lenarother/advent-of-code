"""Day 2: Dive!

https://adventofcode.com/2021/day/2

"""
import re

FORWARD = r'forward (\d+)'
UP = r'up (\d+)'
DOWN = r'down (\d+)'


def solve(data):
    up = sum(list(map(int, re.findall(UP, data))))
    down = sum(list(map(int, re.findall(DOWN, data))))
    forward = sum(list(map(int, re.findall(FORWARD, data))))
    return forward, down - up


def instructions(data):
    for i in data.strip().split('\n'):
        yield i


def solve2(data):
    aim = 0
    forward = 0
    depth = 0
    for i in instructions(data):
        if i.startswith('up'):
            v = int(re.findall(UP, i)[0])
            aim -= v
        elif i.startswith('down'):
            v = int(re.findall(DOWN, i)[0])
            aim += v
        elif i.startswith('forward'):
            v = int(re.findall(FORWARD, i)[0])
            forward += v
            depth += aim * v
    return forward, depth


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    x, y = solve(input_data)
    print(f'Example1: {x * y}')

    input_data = open('input_data.txt').read()
    x, y = solve2(input_data)
    print(f'Example2: {x * y}')
