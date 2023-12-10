"""Day 10: Pipe Maze

https://adventofcode.com/2023/day/10

"""
from santa_helpers.parse import parse_grid_to_dict

POSSIBLE_SHAPES = {
    (-1, 0): ['-', 'L', 'F'],  # LEFT
    (1, 0): ['-', 'J', '7'],  # RIGHT
    (0, -1): ['|', '7', 'F'],  # UP
    (0, 1): ['|', 'J', 'L'],  # DOWN
}

NEIGHBOR_POSITIONS = {
    '-': [(-1, 0), (1, 0)],
    '|': [(0, -1), (0, 1)],
    '7': [(-1, 0), (0, 1)],
    'J': [(0, -1), (-1, 0)],
    'L': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)],
    'S': [(1, 0), (0, 1), (-1, 0), (0, -1)]
}


def find_start(grid):
    for k, v in grid.items():
        if v == 'S':
            return k


def get_next_position(position, grid, visited):
    shape = grid[position]
    x, y = position
    for dx, dy in NEIGHBOR_POSITIONS[shape]:
        new_position = x + dx, y + dy
        if grid[new_position] in POSSIBLE_SHAPES[(dx, dy)] and new_position not in visited:
            return new_position


def get_path(start, grid):
    path = set()
    current_position = start
    while current_position:
        path.add(current_position)
        current_position = get_next_position(current_position, grid, path)
    return path


def is_contained(position, path, grid):
    if position in path:
        return 0
    right = sorted(list(filter(lambda p: p[0] < position[0] and p[1] == position[1], path)))
    right_signs = [grid[p] for p in right]
    n_up_connections = len(list(filter(lambda x: x in ['|', 'L', 'J'], right_signs)))
    return n_up_connections % 2


def solve(data):
    grid = parse_grid_to_dict(data)
    start = find_start(grid)
    path = get_path(start, grid)
    return len(path) // 2


def solve_2(data):
    grid = parse_grid_to_dict(data)
    start = find_start(grid)
    path = get_path(start, grid)
    return sum([is_contained(position, path, grid) for position in grid])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example2: {result}')
