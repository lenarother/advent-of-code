"""title

https://adventofcode.com/2025/day/4

"""
from santa_helpers.neighbors import neighbors
from santa_helpers.parse import parse_grid_to_dict  # type: ignore


def make_round(data, min_p, max_p):
    can_be_moved = []
    for k, v in data.items():
        roles = 0
        if v == '@':
            for p in neighbors(k, 8, min_p, max_p):
                if data[p] == '@':
                    roles += 1
            if roles < 4:
                can_be_moved.append(k)
    return can_be_moved


def solve(data):
    data = parse_grid_to_dict(data)
    min_p = min(data)
    max_p = max(data)
    return len(make_round(data, min_p, max_p))


def solve2(data):
    result = 0
    data = parse_grid_to_dict(data)
    min_p = min(data)
    max_p = max(data)

    while (to_remove:=make_round(data, min_p, max_p)):
        result += len(to_remove)
        for k in to_remove:
            data[k] = '.'

    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
    result = solve2(input_data)
    print(f'Example2: {result}')
