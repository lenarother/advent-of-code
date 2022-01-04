"""Day 2: I Was Told There Would Be No Math

https://adventofcode.com/2015/day/2

"""
import math
import re

PRESENT = r'(\d+)x(\d+)x(\d+)'


def calc_present_area(lwh):
    l, w, h = list(map(int, lwh))
    return (2 * l * w) + (2 * w * h) + (2 * h * l) + min(l * w, w * h, h * l)


def calculate_ribbon_length(lwh):
    l, w, h = sorted(list(map(int, lwh)))
    return (2 * l) + (2 * w) + math.prod([l, w, h])


def solve(data, calc_function=calc_present_area):
    return sum([calc_function(lwh) for lwh in re.findall(PRESENT, data)])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, calculate_ribbon_length)
    print(f'Example2: {result}')
