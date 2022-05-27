"""Day 11: Hex Ed

https://adventofcode.com/2017/day/11

      \ n  /
    nw +--+ ne
      /    \
    -+      +-
      \    /
    sw +--+ se
      / s  \

"""  # noqa


DIRECTIONS = {
    'n': (0, 1),
    'ne': (1, 0.5),
    'se': (1, -0.5),
    's': (0, -1),
    'sw': (-1, -0.5),
    'nw': (-1, 0.5),
}


def get_direction(ch):
    return DIRECTIONS.get(ch, None)


def find_real_path_points(data):
    x, y = 0, 0
    points = [(x, y)]

    for ch in data.split(','):
        dx, dy = get_direction(ch)
        x += dx
        y += dy
        points.append((x, y))

    return points


def find_target(data):
    return find_real_path_points(data)[-1]


def get_neighbors(positions):
    neighbors = set()
    for p in positions:
        x, y = p
        for ch in DIRECTIONS:
            dx, dy = get_direction(ch)
            neighbors.add((x + dx, y + dy))
    return neighbors


def _get_next_positions(positions, visited):
    neighbors = set()

    for p in positions:
        x, y = p
        for ch in DIRECTIONS:
            dx, dy = get_direction(ch)
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited:
                neighbors.add((x + dx, y + dy))
                visited.add((x + dx, y + dy))

    return neighbors, visited


def find_path_length(target):
    positions = {(0, 0)}
    visited = {(0, 0)}
    counter = 0

    while target not in positions:
        positions, visited = _get_next_positions(positions, visited)
        counter += 1

    return counter


def find_length_of_path_to_furthest_target(data):
    positions = {(0, 0)}
    visited = {(0, 0)}
    counter = 0
    all_points = set(find_real_path_points(data))

    while all_points:
        positions, visited = _get_next_positions(positions, visited)
        all_points -= visited
        counter += 1

    return counter


def solve(data):
    target = find_target(data)
    return find_path_length(target)


def solve2(data):
    return find_length_of_path_to_furthest_target(data)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data.strip())
    print(f'Example1: {result}')

    result = solve2(input_data.strip())
    print(f'Example2: {result}')
