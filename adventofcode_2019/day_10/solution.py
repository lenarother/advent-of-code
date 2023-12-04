"""Day 10:

https://adventofcode.com/2019/day/10

"""
from santa_helpers import parse_grid_to_dict


def get_positions(data):
    return [k for k, v in parse_grid_to_dict(data).items() if v == '#']


def nwd(x, y):
    return abs(nwd(y, x % y) if y else x)


def get_value(x, y):
    if x == 0 and y == 0:
        return 0, 0
    elif x == 0:
        return 0, y // abs(y)
    elif y == 0:
        return x // abs(x), 0
    else:
        nwd_value = nwd(x, y)
        return x // nwd_value, y // nwd_value


def solve(data):
    positions = get_positions(data)
    results = {}
    for x, y in positions:
        values = set()
        for xx, yy in positions:
            dx, dy = xx - x, yy - y
            values.add(get_value(dx, dy))
        print(values)
        results[(x, y)] = len(values) - 1
    return max(results.values())


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

