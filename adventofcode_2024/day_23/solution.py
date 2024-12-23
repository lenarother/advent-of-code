"""Day 23: LAN Party

https://adventofcode.com/2024/day/23

"""
from collections import defaultdict
from itertools import permutations
from copy import copy


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


def extend_triple(bar, data_dict):
    mysets = []
    for i in bar:
        mysets.append(set(data_dict[i]))
    return set.intersection(*mysets)


def solve2(data):
    results = set()
    data_dict = get_data_dict(data)
    triples = find_triples(data)

    to_check = []
    for t in triples:
        #print(t)
        t = set(t)
        foo = extend_triple(t, data_dict)
        for i in foo:
            my_triple = copy(t)
            my_triple.add(i)
            to_check.append(my_triple)

    to_check = set([frozenset(sorted(list(i))) for i in to_check])
    triples = to_check
    #print(triples)

    to_check = []
    for t in triples:
        #print(t)
        t = set(t)
        foo = extend_triple(t, data_dict)
        for i in foo:
            my_triple = copy(t)
            my_triple.add(i)
            to_check.append(my_triple)
    to_check = set([frozenset(sorted(list(i))) for i in to_check])
    triples = to_check

    to_check = []
    for t in triples:
        #print(t)
        t = set(t)
        foo = extend_triple(t, data_dict)
        for i in foo:
            my_triple = copy(t)
            my_triple.add(i)
            to_check.append(my_triple)

    to_check = set([frozenset(sorted(list(i))) for i in to_check])
    triples = to_check

    to_check = []
    for t in triples:
        #print(t)
        t = set(t)
        foo = extend_triple(t, data_dict)
        for i in foo:
            my_triple = copy(t)
            my_triple.add(i)
            to_check.append(my_triple)

    to_check = set([frozenset(sorted(list(i))) for i in to_check])
    #print(to_check)

    triples = to_check

    to_check = []
    for t in triples:
        # print(t)
        t = set(t)
        foo = extend_triple(t, data_dict)
        for i in foo:
            my_triple = copy(t)
            my_triple.add(i)
            to_check.append(my_triple)

    to_check = set([frozenset(sorted(list(i))) for i in to_check])
    # print(to_check)
    triples = to_check

    to_check = []
    for t in triples:
        # print(t)
        t = set(t)
        foo = extend_triple(t, data_dict)
        for i in foo:
            my_triple = copy(t)
            my_triple.add(i)
            to_check.append(my_triple)

    to_check = set([frozenset(sorted(list(i))) for i in to_check])
    # print(to_check)

    triples = to_check

    to_check = []
    for t in triples:
        # print(t)
        t = set(t)
        foo = extend_triple(t, data_dict)
        for i in foo:
            my_triple = copy(t)
            my_triple.add(i)
            to_check.append(my_triple)

    to_check = set([frozenset(sorted(list(i))) for i in to_check])
    # print(to_check)

    triples = to_check

    to_check = []
    for t in triples:
        # print(t)
        t = set(t)
        foo = extend_triple(t, data_dict)
        for i in foo:
            my_triple = copy(t)
            my_triple.add(i)
            to_check.append(my_triple)

    to_check = set([frozenset(sorted(list(i))) for i in to_check])
    # print(to_check)

    triples = to_check

    to_check = []
    for t in triples:
        # print(t)
        t = set(t)
        foo = extend_triple(t, data_dict)
        for i in foo:
            my_triple = copy(t)
            my_triple.add(i)
            to_check.append(my_triple)

    to_check = set([frozenset(sorted(list(i))) for i in to_check])
    # print(to_check)

    triples = to_check

    to_check = []
    for t in triples:
        # print(t)
        t = set(t)
        foo = extend_triple(t, data_dict)
        for i in foo:
            my_triple = copy(t)
            my_triple.add(i)
            to_check.append(my_triple)

    to_check = set([frozenset(sorted(list(i))) for i in to_check])
    print(to_check)
    print(len(to_check))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example1: {result}')