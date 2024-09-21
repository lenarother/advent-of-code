"""Day 23: A Long Walk

https://adventofcode.com/2023/day/23

"""
import copy
import re

ALLOWED_SLOPES = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1),
}

from santa_helpers import parse_grid_to_dict
from santa_helpers.neighbors import NEIGHBORS_N, is_point_in_range


def neighbors(p, n=4, p_min=None, p_max=None):
    """Point neighbor generator.

    Args:
        p: tuple (x, y)
        n: int 4 (no diagonal) or 8 (with diagonal)
        p_min (optional): min grid point, if not given infinite
        p_max (optional): max grid point, if not given infinite

    Yields:
        point (x, y)
    """
    neighbor_points = NEIGHBORS_N[n]
    x, y = p
    for dx, dy in neighbor_points:
        new_p = (x + dx, y + dy)
        if is_point_in_range(new_p, p_min, p_max):
            yield new_p, (dx, dy)


def possible_steps(current, grid, visited):
    for position, direction in neighbors(current):
        # print(position, direction)
        if position not in grid:
            continue
        if position in visited:
            continue
        if grid[position] == '#':
            continue
        if (
            grid[position] in ALLOWED_SLOPES
        ):
            if ALLOWED_SLOPES[grid[position]] != direction:
                continue
        if (
            grid[current] in ALLOWED_SLOPES and
            ALLOWED_SLOPES[grid[current]] != direction
        ):
            continue
        yield position


def solve(data, start=(1, 0), target=(21, 22), clean_slopes=False):
    if clean_slopes:
        data = re.sub(r'[<>^v]','.', data)

    grid = parse_grid_to_dict(data)
    results = []
    paths = [[set(), start]]

    while paths:
        path = paths.pop()
        visited = path[0]
        last_position = path[-1]

        if last_position == target:
            results.append(len(visited))
            continue

        steps = list( possible_steps(last_position, grid, visited))
        while len(steps) == 1:
            visited.add(last_position)
            last_position = steps[0]
            steps = list(possible_steps(last_position, grid, visited))

        if last_position == target:
            results.append(len(visited))
            continue

        for p in possible_steps(last_position, grid, visited):
            new_visited = copy.copy(visited)
            new_visited.add(last_position)
            paths.append([new_visited, p])
    return max(results)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data, start=(1, 0), target=(139, 140))
    print(f'Example1: {result}')
