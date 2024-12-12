"""Day 12: Garden Groups

https://adventofcode.com/2024/day/12

"""
NEIGHBORS = [
           (0, -1),         # noqa
    (-1, 0),       (1, 0),  # noqa
           (0,  1),         # noqa
]

NEIGHBORS_8 = [
    (-1, -1), (0, -1), (1, -1),  # noqa
    (-1,  0),          (1,  0),  # noqa
    (-1,  1), (0,  1), (1,  1),  # noqa
]

DIAGONALS = [
    (-1, -1),       (1, -1),  # noqa
                              # noqa
    (-1, 1),         (1, 1),  # noqa

]


def neighbors(p):
    """Point neighbor generator.

    Yields:
        point (x, y)
    """
    x, y = p
    for dx, dy in NEIGHBORS:
        yield x + dx, y + dy


def neighbors_8(p):
    """Point neighbor generator.

    Yields:
        point (x, y)
    """
    x, y = p
    for dx, dy in NEIGHBORS_8:
        yield x + dx, y + dy


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
            if n in grid and n not in region and n not in todo and grid[n] == region_type:
                todo.append(n)
        region.append(p)
        grid.pop(p)
    return region, region_type


def get_top_left(region_coord_list):
    min_coord_sum = 1_000_000
    coord = None
    for x, y in region_coord_list:
        if x + y < min_coord_sum:
            min_coord_sum = x + y
            coord = (x, y)
    return coord

def is_next_to_region(p, region):
    if p in region:
        return False
    for n in neighbors_8(p):
        if n in region:
            return True
    return False


def get_fence_coord(region):
    fence = []
    top_left = get_top_left(region)
    x, y = top_left
    first = (x, y - 1)
    current = first
    can_make_step = True
    while can_make_step:
        fence.append(current)
        can_make_step = False
        for n in neighbors(current):
            if n not in fence and n not in region and is_next_to_region(n, region):
                current = n
                can_make_step = True
                break
    return fence

    #go right


def solve(data):
    from copy import copy
    grid = get_grid_dict(data.strip())
    grid_bkp = copy(grid)
    print(grid)
    regions = []
    region_types = []
    while len(grid):
        region, region_type = get_region(grid)
        regions.append(region)
        region_types.append(region_type)

    print(regions, region_types)
    for r, ch in zip(regions, region_types):
        print('------------')
        print(f'{ch} {get_top_left(r)}')
        print(len(get_fence_coord(r)))
        print('------------')

    return data


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
