"""Day 3: Crossed Wires

https://adventofcode.com/2019/day/3

"""
from santa_helpers.distances import manhattan
from santa_helpers.paths import path_points


def get_wire_points(wire):
    points = []
    current = (0, 0)
    for x in wire.strip().split(','):
        current_points = list(path_points(current, x))
        points.extend(current_points)
        current = current_points[-1]
    return points


def get_common_points(wire1_points, wire2_points):
    return set(wire1_points).intersection(set(wire2_points))


def solve(data):
    wire1, wire2 = data.strip().split('\n')
    wire1_points = get_wire_points(wire1)
    wire2_points = get_wire_points(wire2)
    common = get_common_points(wire1_points, wire2_points)
    return min([manhattan((0, 0), x) for x in common])


def solve2(data):
    wire1, wire2 = data.strip().split('\n')
    wire1_points = get_wire_points(wire1)
    wire2_points = get_wire_points(wire2)
    common = get_common_points(wire1_points, wire2_points)
    return min([
        wire1_points.index(p) + wire2_points.index(p)
        for p in common
    ]) + 2


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')