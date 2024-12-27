"""Day 12: Garden Groups

https://adventofcode.com/2024/day/12

"""
from collections import defaultdict

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


def neighbors_with_direction(p):
    """Point and direction neighbor generator.
    Directions are N, W, E, S
    Yields:
        point (x, y), direction
    """
    directions = ['N', 'W', 'E', 'S']
    x, y = p
    for (dx, dy), d in zip(NEIGHBORS, directions):
        yield (x + dx, y + dy), d


def get_grid_dict(data):
    return {
        (x, y): v
        for y, row in enumerate(data.strip().split('\n'))
        for x, v in enumerate(row.strip())
    }


def get_region(grid):
    first_key = list(grid.keys())[0]
    region_type = grid[first_key]
    region = []
    todo = [first_key]
    while todo:
        p = todo.pop()
        for n in neighbors(p):
            if (
                    n in grid
                    and n not in region
                    and n not in todo
                    and grid[n] == region_type
            ):
                todo.append(n)
        region.append(p)
        grid.pop(p)
    return region, region_type


def get_fence_count(region):
    fence = 0
    for p in region:
        for n in neighbors(p):
            if n not in region:
                fence += 1
    return fence


def _get_top_left(region_coord_list):
    min_coord_sum = 1_000_000
    coord = None
    for x, y in region_coord_list:
        if x + y < min_coord_sum:
            min_coord_sum = x + y
            coord = (x, y)
    return coord


def get_walls_dict(region):
    walls_dict = defaultdict(list)
    for p in region:
        for n, d in neighbors_with_direction(p):
            if n not in region:
                walls_dict[d].append(n)
    return walls_dict


def remove_wall(walls):
    first_piece = _get_top_left(walls)
    walls.remove(first_piece)
    x, y = first_piece

    if (x + 1, y) in walls:
        x = x + 1
        while (x, y) in walls:
            walls.remove((x, y))
            x = x + 1

    elif (x, y + 1) in walls:
        y = y + 1
        while (x, y) in walls:
            walls.remove((x, y))
            y = y + 1

    return walls


def solve(data):
    result = 0
    grid = get_grid_dict(data.strip())
    regions = []
    region_types = []
    while len(grid):
        region, region_type = get_region(grid)
        regions.append(region)
        region_types.append(region_type)
    for r, ch in zip(regions, region_types):
        result += len(r) * get_fence_count(r)
    return result


def solve2(data):
    result = 0
    grid = get_grid_dict(data.strip())
    regions = []
    region_types = []
    while len(grid):
        region, region_type = get_region(grid)
        regions.append(region)
        region_types.append(region_type)
    for r, ch in zip(regions, region_types):
        area = len(r)
        walls_dict = get_walls_dict(r)
        wall_count = 0
        for d in ['N', 'W', 'E', 'S']:
            walls = walls_dict[d]
            while walls:
                walls = remove_wall(walls)
                wall_count += 1
        result += area * wall_count
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
