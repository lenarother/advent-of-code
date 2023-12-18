"""Day 18: Lavaduct Lagoon

https://adventofcode.com/2023/day/18

"""
DIRECTIONS = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
}

def parse_data(data):
    for l in data.strip().split('\n'):
        l = l.split()
        yield l[0], int(l[1]), l[2]


def get_points(start_position, direction, length, grid):
    dx, dy = DIRECTIONS[direction]
    x, y = start_position
    new_x = x
    new_y = y
    for i in range(0, length):
        grid[(new_x, new_y)] = direction
        new_x = new_x + dx
        new_y = new_y + dy
    return new_x, new_y


def get_grid(data):
    grid = {}
    next_start = (0, 0)
    for direction, length, _ in parse_data(data):
        next_start = get_points(next_start, direction, length, grid)
    return grid


def get_path(grid):
    return list(grid.keys())


def get_size(grid):
    xs = []
    ys = []
    for i in grid:
        xs.append(i[0])
        ys.append(i[1])
    return (min(xs), min(ys)), (max(xs), max(ys))


def print_grid(grid, internals):
    grid_str = '\n'
    p_min, p_max = get_size(grid)
    for y in range(p_min[1], p_max[1] + 1):
        for x in range(p_min[0], p_max[0] + 1):
            if (x, y) in grid:
                grid_str += '#'
            elif (x, y) in internals:
                grid_str += '#'
            else:
                grid_str += '.'

        grid_str += '\n'
    grid_str += '\n'
    return grid_str


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
        return

    # Find all path elements to the right from given point.
    right = filter(lambda p: p[0] < position[0] and p[1] == position[1], path)
    right_signs = [grid[p] for p in right]

    # Calculate how many element going up lay on the right side from the point.
    #  - even -> point is not contained
    #  - uneven -> point is contained
    n_up = len(list(filter(lambda x: x in ['U'], right_signs)))
    return n_up % 2


def solve(data):
    grid = get_grid(data)
    path = set(get_path(grid))
    p_min, p_max = get_size(grid)

    internals = {}

    for y in range(p_min[1], p_max[1] + 1):
        for x in range(p_min[0], p_max[0] + 1):
            if is_contained((x, y), path, grid):
                internals[(x, y)] = True
    print(print_grid(grid, internals))
    return len(grid) + len(internals)




if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
