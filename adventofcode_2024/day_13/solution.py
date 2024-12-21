"""Day 13: Claw Contraption

https://adventofcode.com/2024/day/13

"""
import re
from itertools import permutations, product
import math


def solve_single(ax, ay, bx, by, x, y):
    ax, ay, bx, by, x, y = int(ax), int(ay), int(bx), int(by), int(x), int(y)
    button_a = {i: (i * ax, i * ay) for i in range(101)}
    button_b = {i: (i * bx, i * by) for i in range(101)}

    for i, j in product(range(101), range(101)):
        if button_a[i][0] + button_b[j][0] == x and button_a[i][1] + button_b[j][1] == y:
            return i * 3 + j * 1
    return 0


def solve(data):
    data = re.findall(
        r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
        data,
    )
    return sum([solve_single(ax, ay, bx, by, x, y) for ax, ay, bx, by, x, y in data])


def solve3(data):
    data = re.findall(
        r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
        data,
    )
    result = 0
    for ax, ay, bx, by, x, y in data:
        ax, ay, bx, by, x, y = int(ax), int(ay), int(bx), int(by), int(x) + 10_000_000_000_000, int(y) + 10000000000000

        max_but_a = min([x // ax, y // ay])
        while max_but_a:

            rest_x, rest_y = x - ax * max_but_a, y - ay * max_but_a
            if rest_x % bx and rest_y % by and rest_x // bx == rest_y // by:
                result += (3 * max_but_a) + rest_x // bx
            max_but_a -= 1

    return result

def solve_single_2(ax, ay, bx, by, x, y):
        ax, ay, bx, by, x, y = int(ax), int(ay), int(bx), int(by), int(x), int(y)
        button_a = {i: (i * ax, i * ay) for i in range(101)}
        button_b = {i: (i * bx, i * by) for i in range(101)}

        for i, j in product(range(101), range(101)):
            if x % (button_a[i][0] + button_b[j][0]) == 0 and y % (button_a[i][1] + button_b[j][1]) == 0:
                return i * 3 * (x // (button_a[i][0] + button_b[j][0])) + j * 1 * (y // (button_a[i][1] + button_b[j][1]) )
        return 0

def solve2(data):
        data = re.findall(
            r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
            data,
        )
        return sum([solve_single_2(ax, ay, bx, by, x, y) for ax, ay, bx, by, x, y in data])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
