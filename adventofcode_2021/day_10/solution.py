"""Day 10: Syntax Scoring

https://adventofcode.com/2021/day/10

"""
PAIRS = {
    '{': '}',
    '<': '>',
    '[': ']',
    '(': ')',
}

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

POINTS_AUTOCOMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def parse_line(line):
    parsed = []
    for ch in line:
        if ch in '(<[{':
            parsed.append(ch)
        else:
            opening = parsed.pop()
            if PAIRS[opening] != ch:
                return ch
    return parsed


def calc_autocomplete_points(line):
    rest = parse_line(line)
    points = 0
    if isinstance(rest, str):  # invalid character
        return points
    while rest:
        ch = PAIRS.get(rest.pop(), 0)
        points = (points * 5) + POINTS_AUTOCOMPLETE.get(ch)
    return points


def solve(data):
    return sum([
        POINTS.get(str(parse_line(line)), 0)
        for line in data.strip().split()
    ])


def solve2(data):
    points = [
        calc_autocomplete_points(line)
        for line in data.strip().split()
    ]
    points = list(filter(lambda x: x != 0, points))
    points.sort()
    return points[len(points) // 2]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
