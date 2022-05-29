"""Day 14: Disk Defragmentation

https://adventofcode.com/2017/day/14

"""
from functools import reduce

from santa_helpers import neighbors

###################
# KNOT HASH START #
###################


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


def prepare_input(data, repeats=64):
    suffix = [17, 31, 73, 47, 23]
    asci_input = [ord(i) for i in data.strip()]
    return (asci_input + suffix) * repeats


def densify(data):
    n = 16
    dens = []
    while n <= len(data):
        dens.append(reduce(lambda i, j: i ^ j, data[(n - 16):n]))
        n += 16
    return dens


def create_knot_hash(data, size=256):
    lengths = prepare_input(data)
    result_list = create_hash(size, lengths)
    dense_list = densify(result_list)
    return ''.join([f'{bla:#04x}'[2:] for bla in dense_list])

#################
# KNOT HASH END #
#################


def get_row_bits(key_string, n):
    h = create_knot_hash(f'{key_string}-{n}')
    return list(map(int, bin(int(h, 16))[2:].zfill(128)))


def solve(data):
    counter = 0
    for i in range(128):
        counter += sum(get_row_bits(data, i))
    return counter


def get_occupied_addresses(data):
    points = set()

    for y in range(128):
        bin_hash = get_row_bits(data, y)
        for x in range(len(bin_hash)):
            if bin_hash[x]:
                points.add((x, y))

    return points


def solve2(data):
    points = get_occupied_addresses(data)
    group_count = 0
    group = set()

    while points:
        if not group:
            next_p = points.pop()
            group.add(next_p)
            group_count += 1

        nb = set()
        for g in group:
            for p in neighbors(g, 4):
                nb.add(p)

        next_group = points.intersection(nb)
        points -= next_group
        group = next_group

    return group_count


if __name__ == '__main__':
    input_data = 'amgozmfv'

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
