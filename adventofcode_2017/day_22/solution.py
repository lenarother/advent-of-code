"""Day 22: Sporifica Virus

https://adventofcode.com/2017/day/22

"""
import math

from santa_helpers.parse import parse_grid_to_dict

DIRECTIONS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

CLEAN = '.'
INFECTED = '#'
WEAKENED = 'W'
FLAGGED = 'F'

STATE_CHANGE_MAP_1 = {
    CLEAN: INFECTED,
    INFECTED: CLEAN,
}

STATE_CHANGE_MAP_2 = {
    CLEAN: WEAKENED,
    WEAKENED: INFECTED,
    INFECTED: FLAGGED,
    FLAGGED: CLEAN,
}


def parse(grid):
    return parse_grid_to_dict(grid)


def get_center_point(grid):
    """Start point for simulation"""
    x = int(math.sqrt(len(grid)) // 2)
    return x, x


def turn_right(direction):
    directions = 'LDRU'
    i = directions.index(direction)
    return directions[i - 1]


def turn_left(direction):
    directions = 'URDL'
    i = directions.index(direction)
    return directions[i - 1]


def no_turn(direction):
    return direction


def turn_reverse(direction):
    directions = 'URDL'
    i = directions.index(direction)
    return directions[i - 2]


def turn(direction, state):
    turns_map = {
        CLEAN: turn_left,
        WEAKENED: no_turn,
        INFECTED: turn_right,
        FLAGGED: turn_reverse,
    }
    return turns_map[state](direction)


def get_state(position, grid):
    if position not in grid:
        grid[position] = '.'
    return grid[position]


def change_state(state, states_map):
    return states_map[state]


def step(position, direction):
    x, y = position
    dx, dy = DIRECTIONS[direction]
    return x + dx, y + dy


def burst(grid, states_map):
    position = get_center_point(grid)
    direction = 'U'
    infections = 0

    while 1:
        state = get_state(position, grid)
        direction = turn(direction, state)
        new_state = change_state(state, states_map)
        if new_state == INFECTED:
            infections += 1
        grid[position] = new_state
        position = step(position, direction)
        yield infections


def solve(data, n, states_map):
    grid = parse(data)
    b = burst(grid, states_map)

    while n:
        infected = next(b)
        n -= 1

    return infected


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data, 10_000, STATE_CHANGE_MAP_1)
    print(f'Example1: {result}')

    result = solve(input_data, 10_000_000, STATE_CHANGE_MAP_2)
    print(f'Example2: {result}')
