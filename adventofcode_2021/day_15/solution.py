"""Day 15: Chiton

https://adventofcode.com/2021/day/15

Dijkstry Algorithm:
https://pl.wikipedia.org/wiki/Algorytm_Dijkstry
"""
from collections import defaultdict


class Cave:
    MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    INFINITY = 9999

    def __init__(self, data):
        self.start = (0, 0)

        self.weight = dict()
        self.distance = dict()
        self.distance_lookup = defaultdict(set)

        self.size_x = None
        self.size_y = None
        self.exit = None

        if data:
            self._parse(data)
            self._set_initial_distance()
            self._set_initial_distance_lookup()

    def _parse(self, data):
        rows = data.strip().split('\n')

        self.size_y = len(rows)
        self.size_x = len(rows[0].strip())
        self.exit = (self.size_x - 1, self.size_y - 1)

        for y, row in enumerate(rows):
            for x, val in enumerate(list(row.strip())):
                self.weight[(x, y)] = int(val)

    def _set_initial_distance(self):
        for pos in self.weight:
            if pos == self.start:
                self.distance[pos] = 0
            else:
                self.distance[pos] = self.INFINITY

    def _set_initial_distance_lookup(self):
        self.distance_lookup[self.INFINITY] = set(self.distance.keys())
        self.distance_lookup[self.INFINITY] -= {self.start}
        self.distance_lookup[0] = {self.start}

    def get_position_with_min_cost(self):
        min_cost = min(self.distance_lookup.keys())
        position = self.distance_lookup[min_cost].pop()
        if len(self.distance_lookup[min_cost]) == 0:
            del self.distance_lookup[min_cost]
        return position

    def get_adj_positions(self, position):
        x, y = position
        for move in self.MOVES:
            dx, dy = move
            x_check, y_check = x + dx, y + dy
            if self.size_x > x_check >= 0 and self.size_y > y_check >= 0:
                yield x_check, y_check

    def update_distance_lookup(self, pos, current_distance, new_distance):
        self.distance_lookup[current_distance] -= {pos}
        if len(self.distance_lookup[current_distance]) == 0:
            del self.distance_lookup[current_distance]
        self.distance_lookup[new_distance].add(pos)

    def relax(self, pos):
        for adj_pos in self.get_adj_positions(pos):
            current_distance = self.distance[adj_pos]
            new_distance = self.distance[pos] + self.weight[adj_pos]

            if current_distance > new_distance:

                self.distance[adj_pos] = new_distance
                self.update_distance_lookup(
                    adj_pos,
                    current_distance,
                    new_distance
                )

    def walk(self):
        while len(self.distance_lookup) > 0:
            pos = self.get_position_with_min_cost()
            self.relax(pos)
        return self.distance[self.exit]


def solve(data):
    c = Cave(data)
    return c.walk()


def increase_row(row, n=1):
    while n:
        row = ''.join([
            '1' if ch == '9'
            else str((int(ch) + 1))
            for ch in row
        ])
        n -= 1
    return row


def extend_input(data, n=5):
    rows = data.strip().split('\n')
    new_rows = []
    for i in range(n):
        for r in rows:
            new_rows.append(increase_row(r, i))
    new_input = ''
    for r in new_rows:
        new_input += ''.join([increase_row(r, i) for i in range(n)])
        new_input += '\n'
    return new_input


def solve2(data):
    new_data = extend_input(data.strip(), 5)
    c = Cave(new_data)
    return c.walk()


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
