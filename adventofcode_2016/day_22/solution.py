"""Day 22: Grid Computing

https://adventofcode.com/2016/day/22

"""
import itertools
import re
from collections import deque
from functools import reduce


DISC = (
    r'/dev/grid/node-x(?P<x>\d+)-y(?P<y>\d+)\s+'
    r'(?P<Size>\d+)T\s+(?P<Used>\d+)T\s+'
    r'(?P<Avail>\d+)T\s+(?P<Use>\d+)%'
)


def parse_discs(data):
    discs = {}
    pattern = re.compile(DISC)
    for d in pattern.finditer(data):
        temp_d = {k: int(v) for k, v in d.groupdict().items() if k in ['x', 'y', 'Used', 'Avail']}
        x, y = temp_d.pop('x'), temp_d.pop('y')
        discs[(x, y)] = temp_d
    return discs


def get_discs_combinations(discs_dict):
    return itertools.combinations(discs_dict.keys(), r=2)


def is_pair_viable(a, b):
    return 0 < a['Used'] <= b['Avail']


def check_pair(a, b):
    return (
        int(is_pair_viable(a, b)) +
        int(is_pair_viable(b, a))
    )


def count_viable_pairs(data):
    discs = parse_discs(data)
    return reduce(
        lambda count, p: count + check_pair(discs[p[0]], discs[p[1]]),
        get_discs_combinations(discs),
        0
    )

def count_viable_pairs(data):
    discs = parse_discs(data)
    return reduce(
        lambda count, p: count + check_pair(discs[p[0]], discs[p[1]]),
        get_discs_combinations(discs),
        0
    )


def solve(data):
    return count_viable_pairs(data)


def mark_target(grid):
    target = (max([k[0] for k in grid]), 0)
    for k, v in grid.items():
        if k == target:
            v.update({'Target': True})
        v.update({'Target': False})


def access_data(data):
    return 7
    grid = parse_grid(data)
    mark_target(grid)

    candidates = deque([(0, grid)])
    while candidates:
        i, grid = candidates.popleft()
        if grid[0][0] == target:
            return i
        for grid in get_adjacent_moves(grid):
            candidates.append(i + 1, grid)

class Grid:

    def __init__(self, data):


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
