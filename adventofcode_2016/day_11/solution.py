""""Radioisotope Thermoelectric Generators"

https://adventofcode.com/2016/day/11

"""

import re
from collections import Counter, OrderedDict, defaultdict, deque
from functools import reduce
from itertools import combinations

ELEVATOR = r'F(\d) E'
ITEM = r'(\w)([GM])'
FLOOR = r'F(\d)'

BITS_VALUES = {
    'H': 1,
    'L': 2,
    'K': 4,
    'C': 8,
    'R': 16,
    'X': 32,
    'D': 64,
}
BITES = [64, 32, 16, 8, 4, 2, 1]


def copy_floor(other):
    f = Floor()
    f.n = other.n
    f.g = other.g
    f.m = other.m
    return f


def copy_building(other):
    b = Building()
    b.elevator = other.elevator
    b.floors = {k: copy_floor(v) for k, v in other.floors.items()}
    b.data = other.data
    b.steps = other.steps
    return b


class Floor:

    def __init__(self):
        self.n = None
        self.g, self.m = None, None

    def __repr__(self):
        return f'<F{self.n} (G: {self.g}, M: {self.m})>'

    def setup(self, data):
        self.n = self.parse_n(data)
        self.g, self.m = self.parse_items_to_bits(data)

    @staticmethod
    def parse_items_to_bits(data):
        bits = {'G': 0, 'M': 0}
        for char, kind in re.findall(ITEM, data):
            bits[kind] += BITS_VALUES[char]
        return bits['G'], bits['M']

    @staticmethod
    def parse_n(data):
        return int(re.findall(FLOOR, data)[0])

    def is_valid(self):
        return not bool((self.m & (255 - self.g)) and self.g)

    def is_empty(self):
        return self.m + self.g == 0

    def items(self):
        temp_g, temp_m = self.g, self.m
        for v in sorted(BITS_VALUES.values(), reverse=True):
            if temp_g >= v:
                temp_g -= v
                yield v, 0
            if temp_m >= v:
                temp_m -= v
                yield 0, v

    def move(self, g, m, direction=1):
        self.g += direction * g
        self.m += direction * m


class Building:

    def __init__(self):
        self.elevator = None
        self.floors = None
        self.data = None
        self.steps = 0

    def setup(self, data):
        self.elevator = self.parse_elevator(data)
        self.floors = self.parse_floors(data)
        self.data = data

    def __repr__(self):
        return f'<B E{self.elevator} ({[str(f) for f in self.floors.values()]})>'

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    @property
    def current_floor(self):
        return self.floors[self.elevator]

    @staticmethod
    def parse_elevator(data):
        return int(re.findall(ELEVATOR, data)[0])

    @staticmethod
    def parse_floors(data):
        floors = OrderedDict()
        for floor_data in data.strip().split('\n')[::-1]:
            floor = Floor()
            floor.setup(floor_data)
            floors[floor.n] = floor
        return floors

    def is_complete(self):
        return all([self.floors[i].is_empty() for i in range(1, 4)])

    def get_possible_moves(self):
        items = list(self.current_floor.items())
        for comb in list(combinations(items, 1)) + list(combinations(items, 2)):
            add_elements = lambda a, b: (a[0] + b[0], a[1] + b[1])
            m = reduce(add_elements, comb, (0, 0))
            yield m, 1
            yield m, -1

    def can_move(self, direction):
        return 1 <= (self.elevator + direction) <= 4

    def move(self, m, direction=1):
        if self.can_move(direction):
            b = copy_building(self)
            b.floors[b.elevator].move(m[0], m[1], -1)
            b.floors[b.elevator + direction].move(m[0], m[1])

            new_floor_valid = b.floors[b.elevator + direction].is_valid()
            current_floor_valid = b.floors[b.elevator].is_valid()

            if new_floor_valid and current_floor_valid:
                b.elevator += direction
                b.steps += 1
                return b

    def get_moves(self):
        moves = self.get_possible_moves()
        for m, direction in moves:
            yield self.move(m, direction)


def parse(data):
    b = Building()
    b.setup(data)
    return b


def solve(data):
    # breadth-first
    b = Building()
    b.setup(data)
    buildings = [b]  # queue
    visited = {b}

    while buildings:
        b = buildings.pop(0)
        for b_new in b.get_moves():
            if b_new and b_new not in visited:
                if b_new.is_complete():
                    return b_new.steps
                visited.add(b_new)
                buildings.append(b_new)
    return -1


if __name__ == '__main__':
    # input_data = open('input_data.txt').read()
    # result = solve(input_data)
    # print(f'Example1: {result}')

    input_data = open('input_data_2.txt').read()
    result = solve(input_data)
    print(f'Example2: {result}')
