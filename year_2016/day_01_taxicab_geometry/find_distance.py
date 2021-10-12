"""Taxicab geometry

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position,
    which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?
"""
import re

DIR = 'NWSE'
DIR_VECTOR = {
    'N': (0, 1),
    'W': (1, 0),
    'S': (0, -1),
    'E': (-1, 0),
}


def get_step(path):
    steps = re.findall(r'([LR])(\d+)', path)
    direction = 0
    x, y = 0, 0

    for lr, s in steps:
        direction += 1 if lr == 'R' else -1
        direction %= 4
        vector = DIR_VECTOR.get(DIR[direction])
        for ds in range(int(s)):
            x += vector[0]
            y += vector[1]
            yield x, y


def get_dist(x, y):
    return abs(x) + abs(y)


def walk(path):
    *_, last = get_step(path)
    return get_dist(*last)


def walk_until_visited(path):
    visited = set()
    for x, y in get_step(path):
        if (x, y) in visited:
            return get_dist(x, y)
        visited.add((x, y))


if __name__ == '__main__':
    test_path = 'R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3'  # noqa

    result = walk(test_path)
    print(f'Example1: {result}')

    result = walk_until_visited(test_path)
    print(f'Example2: {result}')
