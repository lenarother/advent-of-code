"""Day 17: Two Steps Forward

https://adventofcode.com/2016/day/17

"""
from collections import deque
from hashlib import md5

START_POSITION = (0, 0)
END_POSITION = (3, 3)


def get_codes(salt, path):
    return md5(f'{salt}{path}'.encode()).hexdigest()[:4]


def is_open(ch):
    return ch in ['b', 'c', 'd', 'e', 'f']


def is_wall(position):
    return (
        position[0] in [-1, 4] or
        position[1] in [-1, 4]
    )


def get_moves(salt, path, position):
    MOVES = 'UDLR'
    POSITIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    codes = get_codes(salt, path)

    possible_moves = []

    for dp, m, ch in zip(POSITIONS, MOVES, codes):
        if is_open(ch):
            new_position = (position[0] + dp[0], position[1] + dp[1])
            if not is_wall(new_position):
                possible_moves.append((f'{path}{m}', new_position))
    return possible_moves


def find_shortest_path(salt):
    # breadth-first
    paths = deque([
        ('', START_POSITION)
    ])

    while paths:
        path, position = paths.popleft()
        for new_path, new_position in get_moves(salt, path, position):
            if new_position == END_POSITION:
                return new_path
            paths.append((new_path, new_position))
    return -1


def find_longest_path(salt):
    # breadth-first
    length = 0
    paths = deque([
        ('', START_POSITION)
    ])

    while paths:
        path, position = paths.popleft()
        for new_path, new_position in get_moves(salt, path, position):
            if new_position == END_POSITION:
                if len(new_path) > length:
                    length = len(new_path)
            else:
                paths.append((new_path, new_position))
    return length


def solve(salt, longest=False):
    if longest:
        return find_longest_path(salt)
    return find_shortest_path(salt)


if __name__ == '__main__':
    result = solve('yjjvjgan')
    print(f'Example1: {result}')

    result = solve('yjjvjgan', True)
    print(f'Example2: {result}')
