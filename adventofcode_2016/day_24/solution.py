"""Day 24: Air Duct Spelunking

https://adventofcode.com/2016/day/24

"""
import itertools
import re

LOCATION = r'[.#]?(\d)[.#]?'


class Maze:
    MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    WALKABLE = '.y1234567890'

    def __init__(self, maze):
        self.maze = maze.lower().strip().split()
        self.start = None
        self.end = None

    def __iter__(self):
        for y, y_el in enumerate(self.maze):
            for x, x_el in enumerate(y_el):
                yield (x, y), x_el

    def find_position(self, element):
        for position, el in self:
            if el == element:
                return position

    def find_moves(self, position):
        possible_moves = set()
        x, y = position
        for move in self.MOVES:
            dx, dy = move
            x_check, y_check = x + dx, y + dy
            if self.maze[y_check][x_check] in self.WALKABLE:
                possible_moves.add((x_check, y_check))
        return possible_moves

    def get_neighbour_positions(self, positions):
        candidates = set()
        for position in positions:
            moves = self.find_moves(position)
            candidates = candidates.union(moves)
        return candidates

    def find_shortest_path(self, max_iter=1000):
        positions = set((self.start,))
        counter = 0

        while self.end not in positions:
            if not max_iter:
                raise MazeException('Max iteration excided.')
            positions = self.get_neighbour_positions(positions)
            counter += 1
            max_iter -= 1

        return counter

    def find_locations(self):
        locations = []
        for row in self.maze:
            locations += re.findall(LOCATION, row)
        return set(locations)


def find_all_paths(maze):
    result = {}
    m = Maze(maze)

    for pair in itertools.combinations(m.find_locations(), 2):
        m = Maze(maze)
        m.start = m.find_position((pair[0]))
        m.end = m.find_position((pair[1]))
        result[frozenset(pair)] = m.find_shortest_path()

    return result


def solve(data, go_back=False):
    paths = find_all_paths(data)
    locations = Maze(data).find_locations()

    shortest_path = None
    for p in itertools.permutations(locations):
        p = list(p)
        if go_back:
            p += ['0']
        if p[0] != '0':
            continue
        path_len = sum([
            paths[frozenset({x, y})]
            for x, y in zip(p[:-1], p[1:])
        ])
        if shortest_path is None or path_len < shortest_path:
            shortest_path = path_len

    return shortest_path


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
