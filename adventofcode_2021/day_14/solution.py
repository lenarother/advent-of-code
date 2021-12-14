"""Day 14: Extended Polymerization

https://adventofcode.com/2021/day/14

"""
import re
from collections import OrderedDict, defaultdict

RULE = r'(\w+) -> (\w)'


def parse(data):
    template, rules_data = data.strip().split('\n\n')
    rules = {k: w for k, w in re.findall(RULE, rules_data)}
    return template, rules


def seq_to_pairs(seq):
    pairs = OrderedDict()
    for i in range(len(seq) - 1):
        k = seq[i:(i + 2)]
        pairs.setdefault(k, 0)
        pairs[k] += 1
    return pairs


def step(pairs, rules):
    new_pairs = OrderedDict()
    for p in pairs:
        ch = rules[p]

        k1 = f'{p[0]}{ch}'
        new_pairs.setdefault(k1, 0)
        new_pairs[k1] += pairs[p]

        k2 = f'{ch}{p[1]}'
        new_pairs.setdefault(k2, 0)
        new_pairs[k2] += pairs[p]
    return new_pairs


def count_letters(pairs):
    letters = defaultdict(int)
    for e, p in enumerate(pairs):
        if e == 0:
            letters[p[0]] += pairs[p]
        letters[p[1]] += pairs[p]
    return letters


def solve(data, steps=10):
    template, rules = parse(data)
    pairs = seq_to_pairs(template)
    while steps:
        pairs = step(pairs, rules)
        steps -= 1
    letters = count_letters(pairs)
    letters_vals = sorted(list(letters.values()))
    return letters_vals[-1] - letters_vals[0]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data, steps=10)
    print(f'Example1: {result}')

    result = solve(input_data, steps=40)
    print(f'Example2: {result}')
