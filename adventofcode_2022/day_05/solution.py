"""Day 5: Supply Stacks

https://adventofcode.com/2022/day/5

Data to move:

        [C] [B] [H]
[W]     [D] [J] [Q] [B]
[P] [F] [Z] [F] [B] [L]
[G] [Z] [N] [P] [J] [S] [V]
[Z] [C] [H] [Z] [G] [T] [Z]     [C]
[V] [B] [M] [M] [C] [Q] [C] [G] [H]
[S] [V] [L] [D] [F] [F] [G] [L] [F]
[B] [J] [V] [L] [V] [G] [L] [N] [J]
 1   2   3   4   5   6   7   8   9
"""
import re
from copy import deepcopy

MOVES_RE = re.compile(r'move (\d+) from (\d+) to (\d+)')
DATA = {
    '1': list('BSVZGPW'),
    '2': list('JVBCZF'),
    '3': list('VLMHNZDC'),
    '4': list('LDMZPFJB'),
    '5': list('VFCGJBQH'),
    '6': list('GFQTSLB'),
    '7': list('LGCZV'),
    '8': list('NLG'),
    '9': list('JFHC'),
}


def moves(moves_data):
    for amount, source, target in MOVES_RE.findall(moves_data):
        yield int(amount), source, target


def make_move(amount, source, target, data):
    for i in range(amount):
        el = data[source].pop()
        data[target].append(el)


def make_move2(amount, source, target, data):
    n = len(data[source]) - amount
    els = data[source][n:]
    data[source] = data[source][:n]
    data[target] += els


def solve(moves_data, data, make_move_function=make_move):
    for amount, source, target in moves(moves_data):
        make_move_function(amount, source, target, data)
    return ''.join(data[k].pop() for k in sorted(data))


if __name__ == '__main__':
    input_moves_data = open('input_data.txt').read()

    input_data = deepcopy(DATA)
    result = solve(input_moves_data, input_data)
    print(f'Example1: {result}')

    input_data = deepcopy(DATA)
    result = solve(input_moves_data, input_data, make_move2)
    print(f'Example1: {result}')
