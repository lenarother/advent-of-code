"""Day 10: Knot Hash

https://adventofcode.com/2017/day/10

"""
from functools import reduce


def create_hash(size, lengths):
    current_list = list(range(size))
    skip_size = 0
    total_skip_size = 0

    for length in lengths:
        selected = current_list[:length]
        rest = current_list[length:]
        selected.reverse()

        position = (length + skip_size) % size
        total_skip_size += length + skip_size
        current_list = selected + rest
        current_list = current_list[position:] + current_list[:position]
        skip_size += 1

    list_start = size - (total_skip_size % size)
    return current_list[list_start:] + current_list[:list_start]


def parse(data):
    return list(map(int, data.strip().split(',')))


def prepare_input(data, repeats=64):
    suffix = [17, 31, 73, 47, 23]
    asci_input = [ord(i) for i in data.strip()]
    return (asci_input + suffix) * repeats


def solve(data, size=256):
    lengths = parse(data)
    result_list = create_hash(size, lengths)
    return result_list[0] * result_list[1]


def densify(data):
    n = 16
    dens = []
    while n <= len(data):
        dens.append(reduce(lambda i, j: i ^ j, data[(n - 16):n]))
        n += 16
    return dens


def solve2(data, size=256):
    lengths = prepare_input(data)
    result_list = create_hash(size, lengths)
    dense_list = densify(result_list)
    return ''.join([hex(x)[2:] for x in dense_list])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example1: {result}')
