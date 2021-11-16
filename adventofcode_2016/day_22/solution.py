"""Day 22: Grid Computing

https://adventofcode.com/2016/day/22

"""
import itertools
import re
from collections import OrderedDict, deque
from copy import deepcopy
from functools import reduce

DISC = (
    r'/dev/grid/node-x(?P<x>\d+)-y(?P<y>\d+)\s+'
    r'(?P<Size>\d+)T\s+(?P<Used>\d+)T\s+'
    r'(?P<Avail>\d+)T\s+(?P<Use>\d+)%'
)
DISC_NULL = r'/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+0T\s+\d+T\s+0%'
DISC_X = r'-x(\d+)-'


def parse_discs(data):
    discs = OrderedDict()
    pattern = re.compile(DISC)
    for d in pattern.finditer(data):
        temp_d = {
            k:
                int(v) for k, v in d.groupdict().items()
                if k in ['x', 'y', 'Used', 'Avail']
        }
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


def solve(data):
    return count_viable_pairs(data)


class Grid:

    def __init__(self, data=None):
        self.width = None
        self.null = None
        self.str_data = None
        self.moves_count = 0
        if data:
            self.parse(data)

    def __repr__(self):
        return self.str_data

    def __hash__(self):
        return (self.str_data)

    def __len__(self):
        return len(self.str_data)

    @staticmethod
    def get_null_coord(data):
        return tuple(map(int, re.findall(DISC_NULL, data)[0]))

    @staticmethod
    def get_width(data):
        return max(map(int, set(re.findall(DISC_X, data)))) + 1

    def parse(self, data):
        self.width = self.get_width(data)
        null_coord = self.get_null_coord(data)
        self.null = null_coord[0] + (null_coord[1] * self.width)
        g_position = (self.width - 1, 0)
        data_dict = parse_discs(data)
        null_disc = data_dict[null_coord]
        self.str_data = ''
        for y in range(int(len(data_dict)/self.width)):
            for x in range(self.width):
                if (x, y) == null_coord:
                    ch = '_'
                elif (x, y) == g_position:
                    ch = 'G'
                elif is_pair_viable(data_dict[(x, y)], null_disc):
                    ch = '.'
                else:
                    ch = '#'
                self.str_data += ch

    def is_completed(self):
        return self.str_data[0] == 'G'

    def is_move_possible(self, m):
        return 0 <= m < len(self) and self.str_data[m] in '.G'

    def get_possible_moves(self):
        moves = [
            self.null - self.width,  # U
            self.null - 1 if self.null % self.width != 0 else None,  # L
            (
                self.null + 1
                if self.null % self.width != (self.width - 1)
                else None
            ),  # R
            self.null + self.width,  # D
        ]
        for m in moves:
            if m is not None and self.is_move_possible(m):
                yield m

    def apply_move(self, m):
        ch = self.str_data[m]
        self.str_data = self.str_data.replace('_', ch)
        self.str_data = self.str_data[:m] + '_' + self.str_data[m + 1:]
        self.null = m
        self.moves_count += 1


def copy_grid(g):
    g_copy = Grid()
    g_copy.null = g.null
    g_copy.width = g.width
    g_copy.str_data = deepcopy(g.str_data)
    g_copy.moves_count = g.moves_count
    return g_copy


def access_data(data):
    grid = Grid(data)
    visited = set()
    visited.add(str(grid))
    candidates = deque([grid])
    while candidates:
        grid = candidates.popleft()
        for m in grid.get_possible_moves():
            new_grid = copy_grid(grid)
            new_grid.apply_move(m)
            if str(new_grid) not in visited:
                if new_grid.is_completed():
                    return new_grid.moves_count
                visited.add(str(new_grid))
                candidates.append(new_grid)
    return -1


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = access_data(input_data)
    print(f'Example2: {result}')
