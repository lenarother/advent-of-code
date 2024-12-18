"""Day 18: RAM Run

https://adventofcode.com/2024/day/18

"""
from copy import copy

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


def bytes_gen(data, n):
    data = data.strip().split('\n')
    counter = 0
    while n:
        current = data[counter].split(',')
        yield int(current[0]), int(current[1])
        n -= 1
        counter += 1


def in_grid(p, max_p):
    x, y = p
    max_x, max_y = max_p
    return (
        0 <= x <= max_x and
        0 <= y <= max_y
    )


def get_path(bytes, max_p):
    start = (0, 0)
    end = max_p
    paths = [[start]]
    visited = []
    while paths:
        path = paths.pop(0)
        current = path[-1]
        if current == end:
            return path
        else:
            for n in neighbors(current):
                if in_grid(n, max_p) and n not in bytes and n not in visited:
                    new_path = copy(path)
                    new_path.append(n)
                    paths.append(new_path)
                    visited.append(n)


def solve(data, n_bytes, max_p):
    bytes = list(bytes_gen(data, n_bytes))
    return len(get_path(bytes, max_p)) - 1


def solve2(data, n_bytes, max_p):
    while True:
        bytes = list(bytes_gen(data, n_bytes))
        path = get_path(bytes, max_p)
        if not path:
            return bytes[-1]
        n_bytes += 1




if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data, 1024, (70, 70))
    print(f'Example1: {result}')

    result = solve2(input_data, 3024, (70, 70))
    print(f'Example1: {result}')
