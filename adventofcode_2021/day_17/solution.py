"""Day 17: Trick Shot

https://adventofcode.com/2021/day/17

"""
import re

AREA = r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)'


def parse_area(data):
    return list(map(int, re.findall(AREA, data)[0]))


def in_target(pos, target):
    x, y = pos
    x_min, x_max, y_min, y_max = target
    return (x_min <= x <= x_max) and (y_min <= y <= y_max)


def may_reach_target(pos, target):
    x, y = pos
    x_min, x_max, y_min, y_max = target
    return x <= x_max and y > y_min


def calculate_step(pos, velocity):
    x, y = pos
    dx, dy = velocity
    x += dx
    y += dy
    dx += 1 if dx < 0 else -1 if dx > 0 else 0
    dy -= 1
    return (x, y), (dx, dy)


def step(velocity):
    pos = (0, 0)
    while 1:
        pos, velocity = calculate_step(pos, velocity)
        yield pos


def get_trajectory(velocity, target):
    positions = []
    steps = step(velocity)
    while 1:
        pos = next(steps)
        if in_target(pos, target):
            positions.append(pos)
            return positions
        elif may_reach_target(pos, target):
            positions.append(pos)
        else:
            return


def trajectory(target):
    x_min, x_max, y_min, y_max = target
    for x in range((2 * x_max) + 1):
        for y in range(- abs(y_min) - 1, abs(y_min) + 1):
            v = (x, y)
            t = get_trajectory(v, target)
            if t:
                yield t


def get_max_y(trajectory):
    return max(trajectory, key=lambda item: item[1])[1]


def solve(data):
    target = parse_area(data)
    max_height = 0
    for t in trajectory(target):
        max_y = get_max_y(t)
        if max_y > max_height:
            max_height = max_y
    return max_height


def solve2(data):
    target = parse_area(data)
    return sum([1 for t in trajectory(target)])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
