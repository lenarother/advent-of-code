"""Day 21: Fractal Art

https://adventofcode.com/2017/day/21

"""
from math import sqrt

PATTERN = '.#...####'


def get_pattern_variants(p):
    p = p.replace('/', '')
    variants = {p}
    if len(p) == 9:
        variants.add(p[2::3] + p[1::3] + p[::3])
        variants.add(p[::3] + p[1::3] + p[2::3])
        variants.add(p[:3][::-1] + p[3:6][::-1] + p[6:][::-1])
    elif len(p) == 4:
        variants.add(p[1::2] + p[::2])
        variants.add(p[::2] + p[1::2])
        variants.add(p[:2][::-1] + p[2:][::-1])
    reversed_variants = {i[::-1] for i in variants}
    variants |= reversed_variants
    return variants


def pattern_repr(pattern):
    pattern = pattern.replace('/', '')
    n = int(sqrt(len(pattern)))
    return '\n'.join([
        pattern[i:i + n]
        for i in range(0, len(pattern), n)
    ])


def parse(data):
    substitution_dict = {}
    for line in data.strip().split('\n'):
        input_pattern, output_pattern = line.split(' => ')
        output_pattern = output_pattern.replace('/', '')
        for pattern in get_pattern_variants(input_pattern):
            substitution_dict[pattern] = output_pattern
    return substitution_dict


def split_pattern(pattern):
    pattern = pattern.replace('/', '')
    n = int(sqrt(len(pattern)))
    size = 2 if n % 2 == 0 else 3
    tail_size = size * n

    fragments = []
    for i in range(0, len(pattern) - (n * (size - 1)), size):
        if i % tail_size < n:  # include only first line
            frag = ''
            x = 0
            while x < size:
                j = i + (x * n)
                frag += pattern[j: j + size]
                x += 1
            fragments.append(frag)

    return fragments


def join_pattern(fragments):
    size = (
        4 if len(fragments[0]) == 16 else
        2 if len(fragments[0]) % 2 == 0 else
        3
    )
    pattern_len = len(fragments[0]) * len(fragments)
    n = int(sqrt(pattern_len))
    pattern = ''

    # Create list of lists
    # Divide each fragment into lines
    fragments_split = []
    for frag in fragments:
        fragments_split.append([
            frag[i:i + size]
            for i in range(0, len(frag), size)
        ])

    # Join lines from fragments preserving right order
    i = 0
    while len(pattern) < pattern_len:
        pattern += fragments_split[i].pop(0)
        if len(pattern) % n == 0:
            i = 0
            fragments_split = list(filter(None, fragments_split))
        else:
            i += 1

    return pattern


def solve(data, n=5, p=PATTERN):
    substitution_dict = parse(data)

    while n:
        fragments = split_pattern(p)
        fragments = [substitution_dict[f] for f in fragments]
        p = join_pattern(fragments)
        n -= 1

    return p.count('#')


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, n=18)
    print(f'Example2: {result}')
