"""Day 13: Claw Contraption

https://adventofcode.com/2024/day/13

"""
import re


def find_best_button_price(ax, ay, bx, by, x, y):
    button_a = (x * by - y * bx) / (by * ax - bx * ay)
    button_b = (y * ax - ay * x) / (ax * by - ay * bx)
    if round(button_a, 2) % 1 == 0 and round(button_b, 2) % 1 == 0:
        return int(3 * button_a + button_b)
    return 0


def solve(data, extend=False):
    data = re.findall(
        r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",  # noqa
        data,
    )
    result = 0
    for ax, ay, bx, by, x, y in data:
        ax, ay, bx, by, x, y = int(ax), int(ay), int(bx), int(by), int(x), int(y)  # noqa
        if extend:
            x += 10_000_000_000_000
            y += 10_000_000_000_000
        result += find_best_button_price(ax, ay, bx, by, x, y)
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, True)
    print(f'Example1: {result}')
