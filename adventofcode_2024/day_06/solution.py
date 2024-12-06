"""Day 6: Guard Gallivant

https://adventofcode.com/2024/day/6

"""

from collections import defaultdict
from copy import copy


def get_grid_dict(data):
    return {
        (x, y): v
        for y, row in enumerate(data.strip().split('\n'))
        for x, v in enumerate(row.strip())
    }


def get_start_position(grid):
    for k, v in grid.items():
        if v == '^':
            return k


def turn_right(direction):
    directions_map = {
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
    }
    return directions_map[direction]


def make_step(position, grid, direction):
    x, y = position
    dx, dy = direction
    new_x = x + dx
    new_y = y + dy
    if (new_x, new_y) not in grid:
        # Outside map, walking finished
        return None, direction
    elif grid[(new_x, new_y)] in '.^':
        # Can go further
        return (new_x, new_y), direction
    elif grid[(new_x, new_y)] == '#':
        # Meet obstruction, need to turn and chenk again
        direction = turn_right(direction)
        return make_step(position, grid, direction)


def get_visited_positions(grid, start_position):
    visited = defaultdict(int)
    position = start_position
    visited[position] = 1  # Include start position
    direction = (0, -1)
    finished = False
    is_loop = False
    while not finished:
        position, direction = make_step(position, grid, direction)
        if not position:
            finished = True
        else:
            visited[position] += 1
        if max(visited.values()) > 4:
            is_loop = True
            finished = True
    return visited, is_loop


def solve(data):
    grid = get_grid_dict(data)
    start_position = get_start_position(grid)
    visited, _ = get_visited_positions(grid, start_position)
    return len(visited)


def grid_generator(grid, visited_grid):
    for k, v in grid.items():
        if k in visited_grid and v == '.':
            new_grid = copy(grid)
            new_grid[k] = '#'
            yield new_grid


def solve2(data):
    grid = get_grid_dict(data)
    start_position = get_start_position(grid)
    visited_positions, _ = get_visited_positions(grid, start_position)
    counter = 0
    for g in grid_generator(grid, visited_positions):
        counter += get_visited_positions(g, start_position)[1]
    return counter


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)

    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
