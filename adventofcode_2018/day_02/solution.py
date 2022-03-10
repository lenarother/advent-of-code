"""Day 2: Inventory Management System

https://adventofcode.com/2018/day/2

"""
from collections import Counter
from itertools import permutations


def solve(data):
    has_2, has_3 = 0, 0
    for row in data.strip().split('\n'):
        letter_counts = Counter(row).values()
        has_2 += 2 in letter_counts
        has_3 += 3 in letter_counts
    return has_2 * has_3


def compare_ids(id, id_other):
    result_id = ''
    counter = 0
    for ch, ch_other in zip(id, id_other):
        if ch == ch_other:
            result_id += ch
        else:
            counter += 1
            if counter > 1:
                return
    return result_id


def solve2(data):
    for pair in permutations(data.strip().split('\n'), 2):
        pair_result = compare_ids(pair[0], pair[1])
        if pair_result:
            return pair_result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
