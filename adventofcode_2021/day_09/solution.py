"""Day 9: Smoke Basin

https://adventofcode.com/2021/day/9

"""


class Cave:
    MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, cave):
        self.cave = cave.lower().strip().split()
        self.max_x = len(self.cave[0]) - 1
        self.max_y = len(self.cave) - 1
        self.lowest_values = {}

    def find_moves(self, position):
        x, y = position
        for move in self.MOVES:
            dx, dy = move
            x_check, y_check = x + dx, y + dy
            if self.max_x >= x_check >= 0 and self.max_y >= y_check >= 0:
                yield x_check, y_check

    def is_point_lowest(self, pos, value=None):
        x, y = pos
        if value is None:
            value = self.cave[y][x]

        for m in self.find_moves(pos):
            nx, ny = m
            nvalue = self.cave[ny][nx]

            if nvalue <= value:
                return False
        return True

    def find_lowest_values(self):
        points = 0
        for y, row in enumerate(self.cave):
            for x, val in enumerate(self.cave[y]):
                if self.is_point_lowest((x, y), val):
                    points += 1 + int(val)
                    self.lowest_values[(x, y)] = val
        return points

    def find_basin(self, pos):
        basin = {pos}

        while 1:
            counter = 0

            to_check = set()
            for p in basin:
                for m in self.find_moves(p):
                    to_check.add(m)

            new_basin = set()

            for m in to_check:
                x, y = m
                v = self.cave[y][x]
                if v != '9' and m not in basin:
                    new_basin.add(m)
                    counter += 1

            basin = basin | new_basin
            if counter == 0:
                return len(basin)

    def find_basins(self):
        basins = []
        self.find_lowest_values()
        for b in self.lowest_values:
            basins.append(self.find_basin(b))
        result = 1
        all_b = sorted(basins, reverse=True)
        for x in all_b[:3]:
            result = result * x
        return result


def solve(data):
    c = Cave(data)
    return c.find_lowest_values()


def solve2(data):
    c = Cave(data)
    return c.find_basins()


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
