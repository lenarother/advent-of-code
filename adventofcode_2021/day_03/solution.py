"""Day 3: Binary Diagnostic

https://adventofcode.com/2021/day/3

"""
from itertools import cycle


def parse_data(data):
    return data.strip().split('\n')


def transpose_list(data):
    return [
        [
            data[j][i]
            for j in range(len(data))
        ]
        for i in range(len(data[0]))
    ]


def find_most_common_bits(bitstring_list):
    return ''.join(
        '0' if b.count('0') > len(b) / 2 else '1'
        for b in transpose_list(bitstring_list)
    )


def reverse_bitstring(bitstring):
    return ''.join([
        str(1 - int(b)) for b in bitstring
    ])


def filter_bitstrings(blist, expected_bit, pos):
    return [b for b in blist if b[pos] == expected_bit]


def find_oxygen(data):
    data = parse_data(data)
    bitstring_len = len(data[0])

    for i in cycle(range(bitstring_len)):
        if len(data) == 1:
            return int(data[0], 2)

        most_common_bits = find_most_common_bits(data)
        data = filter_bitstrings(data, most_common_bits[i], i)


def find_co2(data):
    data = parse_data(data)
    bitstring_len = len(data[0])

    for i in cycle(range(bitstring_len)):
        if len(data) == 1:
            return int(data[0], 2)

        most_common_bits = find_most_common_bits(data)
        less_common_bits = reverse_bitstring(most_common_bits)
        data = filter_bitstrings(data, less_common_bits[i], i)


def solve(data):
    data = parse_data(data)
    x = find_most_common_bits(data)
    y = reverse_bitstring(x)
    return int(x, 2) * int(y, 2)


def solve2(data):
    return find_oxygen(data) * find_co2(data)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = solve2(input_data)
    print(f'Example2: {result}')
