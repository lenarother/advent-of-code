"""Day 19: A Series of Tubes

https://adventofcode.com/2017/day/19

"""
import string

DIRECTIONS = {
    'D': (0, 1),
    'U': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}


def parse(data):
    return [line for line in data.split('\n') if line]


def get_start_coord(data):
    return data[0].index('|'), 0


def get_new_direction(data, p, direction):
    x, y = p
    if direction in 'UD':
        return 'R' if len(data[y][x + 1].strip()) == 1 else 'L'
    return 'D' if len(data[y + 1][x].strip()) == 1 else 'U'


def step_possible(data, p):
    x, y = p
    if y < len(data) and x < len(data[0]):
        return len(data[y][x].strip()) == 1
    return False


def get_next_step(x, y, direction):
    x += DIRECTIONS[direction][0]
    y += DIRECTIONS[direction][1]
    return x, y


def solve(data):
    seq = ''
    data = parse(data)
    x, y = get_start_coord(data)
    direction = 'D'
    n = 1

    while 1:
        x, y = get_next_step(x, y, direction)

        if not step_possible(data, (x, y)):
            break

        content = data[y][x]

        if content in string.ascii_uppercase:
            seq += content

        elif content == '+':
            direction = get_new_direction(data, (x, y), direction)

        n += 1

    return seq, n


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example: {result}')
