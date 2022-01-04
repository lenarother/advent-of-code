"""Day 3: Perfectly Spherical Houses in a Vacuum

https://adventofcode.com/2015/day/3

"""
from collections import defaultdict

DIRECTIONS_MAP = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}


class Santa:

    def __init__(self):
        self.locations = defaultdict(int)
        self.current = (0, 0)
        self.locations[self.current] = 1

    def move(self, ch):
        x, y = self.current
        dx, dy = DIRECTIONS_MAP[ch]
        self.current = (x + dx, y + dy)
        self.locations[self.current] += 1


def solve(data):
    s = Santa()

    for ch in data.strip():
        s.move(ch)

    return len(s.locations)


def solve2(data):
    s1 = Santa()
    s2 = Santa()

    for i, ch in enumerate(data.strip()):
        s1.move(ch) if i % 2 == 0 else s2.move(ch)

    houses = {}
    houses.update(s1.locations)
    houses.update(s2.locations)
    return len(houses)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
