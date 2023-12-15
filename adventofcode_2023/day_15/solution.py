"""Day 15: Lens Library

https://adventofcode.com/2023/day/15

"""
from functools import reduce


def get_ch_hash(start: int, ch: str) -> int:
    return ((start + ord(ch)) * 17) % 256


def get_str_hash(input_str: str) -> int:
    return reduce(get_ch_hash, input_str, 0)


def solve(data: str) -> int:
    return sum([get_str_hash(i) for i in data.strip().split(',')])


def solve_2(data: str) -> int:
    boxes: dict[int, dict] = {
        i: {'labels': list(), 'values': list()}
        for i in range(0, 256)
    }

    for i in data.strip().split(','):
        operation = '-' if '-' in i else '='
        label = i.split(operation)[0]
        box = get_str_hash(label)

        if operation == '-':
            if label in boxes[box]['labels']:
                index = boxes[box]['labels'].index(label)
                del(boxes[box]['labels'][index])
                del(boxes[box]['values'][index])

        elif operation == '=':
            value = int(i.split('=')[1])
            if label in boxes[box]['labels']:
                index = boxes[box]['labels'].index(label)
                boxes[box]['values'][index] = value
            else:
                boxes[box]['labels'].append(label)
                boxes[box]['values'].append(value)

    return sum([
        (box_id + 1) * (position + 1) * value
        for box_id, values in boxes.items()
        for position, value in enumerate(values['values'])
    ])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example1: {result}')
