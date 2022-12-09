"""Day 9: Rope Bridge

https://adventofcode.com/2022/day/9

"""
import re

MOVE_RE = re.compile(r'([RDLU]) (\d+)')

STEP = {
    # direction: (x, y)
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
    # diagonals
    'RD': (1, 1),
    'LD': (-1, 1),
    'RU': (1, -1),
    'LU': (-1, -1),
}


def is_touching(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def get_new_position(p, direction):
    x, y = p
    dx, dy = STEP.get(direction)
    return x + dx, y + dy


def find_direction(h, t):
    xh, yh = h
    xt, yt = t
    x_direction = 'R' if xh > xt else 'L' if xh < xt else ''
    y_direction = 'D' if yh > yt else 'U' if yh < yt else ''
    return x_direction + y_direction


def move_head(h, direction):
    return get_new_position(h, direction)


def move_tail(h, t):
    if is_touching(h, t):
        return t
    direction = find_direction(h, t)
    return get_new_position(t, direction)


def make_step2(h, t1, t2, t3, t4, t5, t6, t7, t8, t9,  direction):
    h = move_head(h, direction)
    t1 = move_tail(h, t1)
    t2 = move_tail(t1, t2)
    t3 = move_tail(t2, t3)
    t4 = move_tail(t3, t4)
    t5 = move_tail(t4, t5)
    t6 = move_tail(t5, t6)
    t7 = move_tail(t6, t7)
    t8 = move_tail(t7, t8)
    t9 = move_tail(t8, t9)
    return h, t1, t2, t3, t4, t5, t6, t7, t8, t9


def moves(data):
    for direction, n in MOVE_RE.findall(data):
        n = int(n)
        while n:
            yield direction
            n -= 1


def solve(data):
    h = (0, 0)
    t = (0, 0)
    visited = {t}
    for direction in moves(data):
        h = move_head(h, direction)
        t = move_tail(h, t)
        visited.add(t)
    return len(visited)


def solve2(data):
    h = (0, 0)
    t1 = (0, 0)
    t2 = (0, 0)
    t3 = (0, 0)
    t4 = (0, 0)
    t5 = (0, 0)
    t6 = (0, 0)
    t7 = (0, 0)
    t8 = (0, 0)
    t9 = (0, 0)

    visited = {t9}
    for direction in moves(data):
        h, t1, t2, t3, t4, t5, t6, t7, t8, t9 = make_step2(
            h, t1, t2, t3, t4, t5, t6, t7, t8, t9, direction
        )
        visited.add(t9)
    return len(visited)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example1: {result}')
