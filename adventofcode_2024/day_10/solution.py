"""Day 10: Hoof It

https://adventofcode.com/2024/day/10

"""
NEIGHBORS = [
           (0, -1),         # noqa
    (-1, 0),       (1, 0),  # noqa
           (0,  1),         # noqa
]


def neighbors(p):
    """Point neighbor generator.

    Yields:
        point (x, y)
    """
    x, y = p
    for dx, dy in NEIGHBORS:
        yield x + dx, y + dy


def get_grid_dict(data):
    return {
        (x, y): int(v)
        for y, row in enumerate(data.strip().split('\n'))
        for x, v in enumerate(row.strip())
    }


def start_position_gen(grid):
    for k, v in grid.items():
        if v == 0:
            yield k


def evaluate_start(start, grid, mode="unique_last_position"):
    result_paths = []
    paths = [[start]]
    while paths:
        p = paths.pop()
        position = p[-1]
        position_val = grid[position]
        for n in neighbors(position):
            if n in grid and (grid[n] - 1) == position_val:
                new_p = p.copy()
                new_p.append(n)
                if grid[n] == 9:
                    result_paths.append(new_p)
                elif new_p not in paths:
                    paths.append(new_p)

    if mode == "unique_last_position":
        return len(set([p[-1] for p in result_paths]))
    elif mode == "unique_paths":
        return len(result_paths)


def solve(data, mode="unique_last_position"):
    grid = get_grid_dict(data)
    return sum([
        evaluate_start(start, grid, mode)
        for start in start_position_gen(grid)
    ])


def solve2(data):
    return solve(data, mode="unique_paths")


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
