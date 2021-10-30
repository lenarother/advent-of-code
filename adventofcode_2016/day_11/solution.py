""""Radioisotope Thermoelectric Generators"

https://adventofcode.com/2016/day/11

"""

import re
from collections import Counter, OrderedDict, defaultdict
from itertools import combinations
from copy import deepcopy

ELEVATOR = r'F(\d) E'
ITEM = r'(\w)([GM])'
FLOOR = r'F(\d)'

BITS_VALUES = {
    'H': 1,
    'L': 2,
}

# change
#    L H R P
# m  0 1 0 1 -> 5
# g  1 1 0 0 -> 12
# b  8 4 2 1


class Floor:

    def __init__(self, n):
        self.n = n
        self.items = set()
        # self.generators
        # self.microchips

    def __repr__(self):
        items = ','.join(sorted(map(str, self.items)))
        return f'<F{self.n} {items}>'.strip()

    def __len__(self):
        return len(self.items)

    def is_valid(self):
        items_dict = defaultdict(str)

        for i in self.items:
            items_dict[i[0]] += i[1]  # 'G' / 'M' / 'GM' / 'MG'
        kind_counts = Counter(items_dict.values())
        return (
            'M' not in kind_counts or (
                'G' not in kind_counts and
                'MG' not in kind_counts and
                'GM' not in kind_counts
            )
        )


class Building:

    def __init__(self, data):
        self.elevator = self.parse_elevator(data)
        self.floors = self.parse_floors(data)
        self.data = data
        self.steps = 0

    def __repr__(self):
        floors = ', '.join([str(f) for f in self.floors.values()])
        return f'<Building E{self.elevator} {floors}>'

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
    def parse_floor(data_floor):
        return Floor(int(re.findall(FLOOR, data_floor)[0]))

    @staticmethod
    def parse_floor_items(data_floor):
        return set([
            f'{char}{kind}'
            for char, kind in re.findall(ITEM, data_floor)
        ])

    def parse_floors(self, data):
        floors = OrderedDict()
        for floor_data in data.strip().split('\n')[::-1]:
            floor = self.parse_floor(floor_data)
            floor.items = self.parse_floor_items(floor_data)
            floors[floor.n] = floor
        return floors

    def is_complete(self):
        for i in range(1, 4):
            if len(self.floors[i]) > 0:
                return False
        return True

    def get_possible_moves(self):
        items = self.current_floor.items
        for comb in list(combinations(items, 1)) + list(combinations(items, 2)):
            yield comb, 1
            yield comb, -1

    def can_move(self, direction):
        return 1 <= (self.elevator + direction) <= 4

    def move(self, items, direction=1):
        if self.can_move(direction):
            b = deepcopy(self)
            for i in items:
                b.floors[b.elevator].items.remove(i)
                b.floors[b.elevator + direction].items.add(i)
            if b.floors[b.elevator + direction].is_valid():
                b.elevator += direction
                b.steps += 1
                return b

    def get_moves(self):
        moves = self.get_possible_moves()
        for m, direction in moves:
            yield self.move(m, direction)


def parse(data):
    return Building(data)


def solve(data):
    # breadth-first
    b = Building(data)
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
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    # input_data = open('input_data_2.txt').read()
    # result = solve(input_data)
    # print(f'Example2: {result}')
