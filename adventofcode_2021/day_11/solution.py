"""Day 11: Dumbo Octopus

https://adventofcode.com/2021/day/11

"""
from itertools import count


class Octopus:
    MOVES = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (-1, 1),
        (1, 1),
        (-1, -1),
        (1, -1),
    ]

    def __init__(self, data):
        self.raw_data = data.strip().split('\n')
        self.data = self.parse(self.raw_data)

    def __repr__(self):
        """For debugging purpose"""
        max_x = len(self.raw_data[0])
        max_y = len(self.raw_data)
        return (
            '\n'.join([
                ''.join([
                    str(self.data[(x, y)])
                    for x in range(max_x)
                ])
                for y in range(max_y)
            ])
        )

    @staticmethod
    def parse(data):
        return {
            (x, y): int(v)
            for y, row in enumerate(data)
            for x, v in enumerate(row)
        }

    def get_adj_positions(self, pos):
        for m in self.MOVES:
            new_pos = (pos[0] + m[0], pos[1] + m[1])
            if new_pos in self.data:
                yield new_pos

    def increase_values(self, positions):
        for p in positions:
            self.data[p] += 1

    def decrease_flashed(self):
        for k, v in self.data.items():
            if v > 9:
                self.data[k] = 0

    def flash(self):
        flashed = set()
        while sum([1 for x in self.data.values() if x > 9]) > len(flashed):
            for k, v in self.data.items():
                if v > 9 and k not in flashed:
                    flashed.add(k)
                    self.increase_values(self.get_adj_positions(k))
        return len(flashed)

    def step(self):
        self.increase_values(self.data.keys())
        flash_count = self.flash()
        self.decrease_flashed()
        return flash_count

    def simulate(self, steps):
        return sum(self.step() for _ in range(steps))

    def simulate2(self):
        for c in count(1):
            if self.step() == 100:
                return c


def solve(data, steps=100):
    octopus_greed = Octopus(data)
    return octopus_greed.simulate(steps)


def solve2(data):
    octopus_greed = Octopus(data)
    return octopus_greed.simulate2()


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = solve2(input_data)
    print(f'Example1: {result}')
