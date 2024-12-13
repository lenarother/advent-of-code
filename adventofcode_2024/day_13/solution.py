"""Day 13: Claw Contraption

https://adventofcode.com/2024/day/13

"""
import re
from itertools import permutations, product


def solve(data):
    data = re.findall(
        r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
        data,
    )
    result = 0
    for ax, ay, bx, by, x, y in data:
        ax, ay, bx, by, x, y = int(ax), int(ay), int(bx), int(by), int(x), int(y)
        button_a = {i: (i * ax, i * ay) for i in range(101)}
        button_b = {i: (i * bx, i * by) for i in range(101)}

        for i, j in product(range(101), range(101)):
            if button_a[i][0] + button_b[j][0] == x and button_a[i][1] + button_b[j][1] == y:
                result += i * 3 + j * 1
                break

    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
