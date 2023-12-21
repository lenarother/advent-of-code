"""Day 21: Step Counter

https://adventofcode.com/2023/day/21

"""
from santa_helpers import neighbors, parse_grid_to_dict


def get_start(grid):
    for k, v in grid.items():
        if v == 'S':
            return k


def get_new_positions(current_positions, grid):
    new_positions = set()
    for p in current_positions:
        for n in neighbors(p, 4):
            if n in grid and grid[n] in 'S.':
                new_positions.add(n)
    return new_positions


def solve(data, steps=6):
    grid = parse_grid_to_dict(data)
    start = get_start(grid)

    possible_positions = {start}
    for i in range(0, steps):
        possible_positions = get_new_positions(possible_positions, grid)

    return len(possible_positions)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 64)
    print(f'Example1: {result}')
