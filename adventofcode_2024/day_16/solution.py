"""Day 16: Reindeer Maze

https://adventofcode.com/2024/day/16

"""
from copy import copy
import heapq

NEIGHBORS = [
                 ((0, -1), 'N'),               # noqa N
    ((-1, 0), 'W'),            ((1, 0), 'E'),  # noqa W E
                 ((0,  1), 'S'),               # noqa S
]

DIRECTIONS = 'NWSE'


def neighbors(p, direction):
    """Point neighbor generator.

    Yields:
        point (x, y)
    """
    x, y = p
    for n in NEIGHBORS:
        position, new_direction = n
        dx, dy = position
        if direction == new_direction:
            cost = 1
        elif DIRECTIONS.index(direction) % 2 == DIRECTIONS.index(new_direction) % 2:
            cost = 2001
        else:
            cost = 1001
        yield ((x + dx, y + dy), new_direction, cost)


def get_grid_dict(data):
    return {
        (x, y): v
        for y, row in enumerate(data.strip().split('\n'))
        for x, v in enumerate(row.strip())
    }

def get_position(grid, ch='S'):
    for k, v in grid.items():
        if v == ch:
            return k


def solve(data):
    grid = get_grid_dict(data)
    start = get_position(grid, 'S')
    end = get_position(grid, 'E')
    direction = 'E'
    ready = []
    paths = [([start], direction, 0)]
    while paths:
        print(len(paths))
        path, direction, score = paths.pop()
        current_position = path[-1]
        if current_position == end:
            ready.append([path, direction, score])
        else:
            for new_position, new_direction, cost in neighbors(current_position, direction):
                if new_position not in path and grid[new_position] in '.E':
                    mypath = copy(path)
                    mypath.append(new_position)
                    paths.append((mypath, new_direction, score + cost))

    return min([i[2] for i in ready])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
