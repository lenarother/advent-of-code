"""Day 3: No Matter How You Slice It

https://adventofcode.com/2018/day/3

"""
import re

CLAIM = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')


def points(start, x, y):
    a, b = start
    for dy in range(y):
        for dx in range(x):
            yield a + dx, b + dy


def get_duplicates(data):
    duplicates = set()
    claims = set()
    for _, ix, iy, x, y in re.findall(CLAIM, data):
        for p in points((int(ix), int(iy)), int(x), int(y)):
            if p in claims and p not in duplicates:
                duplicates.add(p)
            else:
                claims.add(p)
    return duplicates


def solve(data):
    return len(get_duplicates(data))


def solve2(data):
    duplicates = get_duplicates(data)
    for id, ix, iy, x, y in re.findall(CLAIM, data):
        claim_is_dup = False
        for p in points((int(ix), int(iy)), int(x), int(y)):
            if p in duplicates:
                claim_is_dup = True
        if not claim_is_dup:
            return int(id)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
