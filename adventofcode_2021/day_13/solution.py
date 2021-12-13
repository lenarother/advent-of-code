"""Day 13: Transparent Origami

https://adventofcode.com/2021/day/13

"""
import re

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


# todo: instead do fold_dot(dot, instruction) and use python 10
def fold_along_x(dot, val):
    x, y = dot
    new_x = get_value_after_fold(x, val)
    return new_x, y


def fold_along_y(dot, val):
    x, y = dot
    new_y = get_value_after_fold(y, val)
    return x, new_y


def get_dots_after_folding(dots, folds):
    fold_functions = {
        'x': fold_along_x,
        'y': fold_along_y,
    }

    # todo: use reduce
    for fold in folds:
        new_dots = set()
        fold_function = fold_functions[fold[0]]
        fold_value = fold[1]
        for dot in dots:
            new_dots.add(fold_function(dot, fold_value))
        dots = new_dots

    return dots


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
    dots_after_folding = get_dots_after_folding(dots, folds[:1])
    return len(dots_after_folding)


def solve2(data):
    dots, folds = parse(data)
    dots_after_folding = get_dots_after_folding(dots, folds)
    return get_message(dots_after_folding)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve1(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = solve2(input_data)
    print('Example2:')
    print(f'{result}')
