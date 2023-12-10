"""Day 10: Pipe Maze

https://adventofcode.com/2023/day/10

"""
from santa_helpers.parse import parse_grid_to_dict  # type: ignore

# Shapes that one can go into.
# Used to find first step from start point.
POSSIBLE_SHAPES: dict[tuple[int, int], list[str]] = {
    (-1, 0): ['-', 'L', 'F'],  # LEFT
    (1, 0): ['-', 'J', '7'],  # RIGHT
    (0, -1): ['|', '7', 'F'],  # UP
    (0, 1): ['|', 'J', 'L'],  # DOWN
}

# Coordinates connected by shape.
NEIGHBOR_POSITIONS: dict[str, list[tuple[int, int]]] = {
    '-': [(-1, 0), (1, 0)],
    '|': [(0, -1), (0, 1)],
    '7': [(-1, 0), (0, 1)],
    'J': [(0, -1), (-1, 0)],
    'L': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)],
    'S': [(1, 0), (0, 1), (-1, 0), (0, -1)]
}


def find_start(grid: dict[tuple[int, int], str]) -> tuple[int, int]:
    """Return coordinates of start position (indicated by S in input)"""
    for k, v in grid.items():
        if v == 'S':
            return k
    return 0, 0


def get_next_position(
        position: tuple[int, int],
        grid: dict[tuple[int, int], str],
        visited: set[tuple[int, int]]
):
    """Return next step coordinates based on current coordinates."""
    shape = grid[position]
    x, y = position
    for dx, dy in NEIGHBOR_POSITIONS[shape]:
        new_position = x + dx, y + dy
        if (
            grid[new_position] in POSSIBLE_SHAPES[(dx, dy)]  # For start
            and new_position not in visited
        ):
            return new_position


def get_path(start: tuple[int, int], grid: dict[tuple[int, int], str]):
    """Returns coordinates of entire path as set."""
    path = set()
    current_position = start
    while current_position:
        path.add(current_position)
        current_position = get_next_position(current_position, grid, path)
    return path


def is_contained(
        position: tuple[int, int],
        path: set[tuple[int, int]],
        grid: dict[tuple[int, int], str]
) -> int:
    """
    Check if position with given coordinates is contained inside path.

    If yes return 1 if not return 0.
    """
    # If position belongs to path it is not contained.
    if position in path:
        return 0

    # Find all path elements to the right from given point.
    right = filter(lambda p: p[0] < position[0] and p[1] == position[1], path)
    right_signs = [grid[p] for p in right]

    # Calculate how many element going up lay on the right side from the point.
    #  - even -> point is not contained
    #  - uneven -> point is contained
    n_up = len(list(filter(lambda x: x in ['|', 'L', 'J'], right_signs)))
    return n_up % 2


def solve(data: str) -> int:
    """Find distance (n steps) to point most far away."""
    grid = parse_grid_to_dict(data)
    start = find_start(grid)
    path = get_path(start, grid)
    return len(path) // 2


def solve_2(data: str) -> int:
    """Find number of points contained inside the path."""
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
