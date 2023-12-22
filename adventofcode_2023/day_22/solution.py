"""Day 22: Sand Slabs

https://adventofcode.com/2023/day/22

"""


def get_brick_points(brick):
    p1 = list(map(int, brick.split('~')[0].split(',')))
    p2 = list(map(int, brick.split('~')[1].split(',')))

    if p1[0] - p2[0] != 0:
        points = [(i, p1[1], p1[2]) for i in range(p1[0], p2[0] + 1)]
    elif p1[1] - p2[1] != 0:
        points = [(p1[0], i, p1[2]) for i in range(p1[1], p2[1] + 1)]
    elif p1[2] - p2[2] != 0:
        points = [(p1[0], p1[1], i) for i in range(p1[2], p2[2] + 1)]
    else:
        points = [(p1[0], p1[1], p1[2])]

    return points


def sort_brisks(data):
    data = [brick for brick in data.strip().split('\n')]
    sorted_data = sorted(
        data,
        key=lambda brick: int(brick.split('~')[0].split(',')[2])
    )
    return sorted_data


def can_drop(points):
    return (points[0][2] - 1) >= 1


def is_slot_free(points, grid):
    return len(grid.intersection(points)) == 0


def drop(points):
    return [(p[0], p[1], (p[2] - 1)) for p in points]


def get_final_position(points, grid):
    while can_drop(points):
        new_points = drop(points)
        if not is_slot_free(new_points, grid):
            return points
        points = new_points
    return points


def get_belong_to_dict(brick_dict):
    return {
        point: brick
        for brick, points in brick_dict.items()
        for point in points
    }


def get_bricks_above(points, belong_to_dict, brick_name):
    bricks = set()
    points_above = get_points_above(points)
    for point in points_above:
        if point in belong_to_dict:
            name = belong_to_dict[point]
            if name != brick_name:
                bricks.add(belong_to_dict[point])
    return bricks


def get_points_above(points):
    return [(p[0], p[1], (p[2] + 1)) for p in points]


def is_brick_supported(points, grid):
    points_below = drop(points)
    if points_below[0][2] != points_below[-1][2]:  # vertical brick
        points_below = [points_below[0]]
    return len(grid.intersection(points_below)) > 0


def can_remove(points, name, grid, belong_to_dict, bricks_points):
    bricks_above = get_bricks_above(points, belong_to_dict, name)
    if len(bricks_above) == 0:
        return True

    grid_without_points = grid.difference(points)
    for brick in bricks_above:
        if not is_brick_supported(bricks_points[brick], grid_without_points):
            return False
    return True


def solve(data):
    bricks = sort_brisks(data)
    bricks_points = {brick: get_brick_points(brick) for brick in bricks}
    grid = set()

    for brick in bricks:  # list of brick names
        points = get_final_position(bricks_points[brick], grid)
        grid = grid.union(points)
        bricks_points[brick] = points

    belong_to_dict = get_belong_to_dict(bricks_points)
    return sum([
        can_remove(points, name, grid, belong_to_dict, bricks_points)
        for name, points in bricks_points.items()
    ])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
