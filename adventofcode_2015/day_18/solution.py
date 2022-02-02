"""Day 18: Like a GIF For Your Yard

https://adventofcode.com/2015/day/18

"""
from santa_helpers import neighbors, parse_grid_to_dict

ON = '#'
OFF = '.'


def count_neighbors_on(p, grid, max_grid):
    return sum([
        ON == grid[n]
        for n in neighbors(p, 8, p_min=(0, 0), p_max=max_grid)
    ])


def get_light_value(p, grid, max_grid, always_on):
    if p in always_on:
        return ON
    if grid[p] == ON and count_neighbors_on(p, grid, max_grid) in [2, 3]:
        return ON
    if grid[p] == OFF and count_neighbors_on(p, grid, max_grid) == 3:
        return ON

    return OFF


def get_new_grid(grid, max_grid, always_on):
    return {
        p: get_light_value(p, grid, max_grid, always_on)
        for p in grid
    }


def run_simulation(data, steps=100, always_on=None):
    always_on = always_on or set()
    grid = parse_grid_to_dict(data)
    max_grid = max(grid)

    for p in always_on:
        grid[p] = ON

    while steps:
        grid = get_new_grid(grid, max_grid, always_on)
        steps -= 1

    return sum([v == ON for v in grid.values()])


def solve(data, steps=100):
    return run_simulation(data, steps)


def solve2(data, steps=100, always_on=None):
    return run_simulation(data, steps, always_on or {})


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data, 100, {(0, 0), (0, 99), (99, 0), (99, 99)})
    print(f'Example2: {result}')
