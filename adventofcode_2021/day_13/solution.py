"""Day 13: Transparent Origami

https://adventofcode.com/2021/day/13

"""
import re
from functools import reduce

DOT = r'(\d+),(\d+)\n'
FOLD = r'fold along (x|y)=(\d+)'


def parse(data):
    dots = [(int(x), int(y)) for x, y in re.findall(DOT, data)]
    folds = [(d, int(v)) for d, v in re.findall(FOLD, data)]
    return dots, folds


def get_value_after_fold(val, fold_val):
    if val < fold_val:
        return val
    return fold_val - (val - fold_val)


def fold_dot(dot, instruction):
    x, y = dot
    fold_direction, fold_value = instruction

    # Python >= 3.10
    match fold_direction:
        case 'x':
            return get_value_after_fold(x, fold_value), y
        case 'y':
            return x, get_value_after_fold(y, fold_value)

    # Python <= 3.9
    # if fold_direction == 'x':
    #     return get_value_after_fold(x, fold_value), y
    # return x, get_value_after_fold(y, fold_value)


def get_dots_after_folding(dots, folds):
    return reduce(lambda d, f: {fold_dot(dot, f) for dot in d}, folds, dots)


def get_message(dots):
    max_x = max(dots)[0]
    max_y = max(dots, key=lambda item: item[1])[1]

    return '\n'.join([
        ''.join([
            '#' if (x, y) in dots else '.'
            for x in range(max_x + 1)
        ])
        for y in range(max_y + 1)
    ])


def solve1(data):
    dots, folds = parse(data)
    return len(get_dots_after_folding(dots, folds[:1]))


def solve2(data):
    return get_message(get_dots_after_folding(*parse(data)))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve1(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print('Example2:')
    print(f'{result}')
