"""Day 23: LAN Party

https://adventofcode.com/2024/day/23

"""
from collections import defaultdict
from copy import copy
from itertools import permutations


def get_data_dict(data):
    data_dict = defaultdict(list)
    for connection in data.strip().split('\n'):
        i, j = connection.split('-')
        data_dict[i].append(j)
        data_dict[j].append(i)
    return data_dict


def solve(data):
    results = set()
    data_dict = get_data_dict(data)
    for k, v in data_dict.items():
        for x, y in permutations(v, 2):
            if y in data_dict[x]:
                if k.startswith('t') or x.startswith('t') or y.startswith('t'):
                    results.add(tuple(sorted([k, x, y])))
    return len(results)


def find_triples(data):
    results = set()
    data_dict = get_data_dict(data)
    for k, v in data_dict.items():
        for x, y in permutations(v, 2):
            if y in data_dict[x]:
                results.add(tuple(sorted([k, x, y])))
    return results


def extend_group(group, data_dict):
    my_sets = [set(data_dict[i]) for i in group]
    return set.intersection(*my_sets)


def solve2(data):
    data_dict = get_data_dict(data)
    groups = find_triples(data)

    while len(groups) != 1:
        to_check = []
        for group in groups:
            group = set(group)
            foo = extend_group(group, data_dict)
            for i in foo:
                my_group = copy(group)
                my_group.add(i)
                to_check.append(my_group)
        groups = set([frozenset(sorted(list(i))) for i in to_check])

    code = sorted(list(groups.pop()))
    return ','.join(code)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
