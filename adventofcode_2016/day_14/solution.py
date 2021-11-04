"""Day 14: One-Time Pad

https://adventofcode.com/2016/day/14

"""
import re
from hashlib import md5


def get_hash(salt, counter=''):
    return md5(f'{salt}{counter}'.encode()).hexdigest()


def hash_generator(salt):
    counter = 0
    while True:
        yield get_hash(salt, counter)
        counter += 1


def stretch_hash_generator(salt):
    counter = 0
    while True:
        h = get_hash(salt, counter)
        for _ in range(2016):
            h = get_hash(h)
        yield h
        counter += 1


def get_hash_generator(salt, key_stretching=False):
    if key_stretching:
        return stretch_hash_generator(salt)
    return hash_generator(salt)


def get_hash_repeated_char(hash_to_check, repeat_count):
    pattern = r'([0-9a-f])' + (r'\1' * (repeat_count - 1))
    repeated = re.findall(pattern, hash_to_check)
    return repeated[0] if len(repeated) > 0 else None


def ahead_lookup_generator(salt, key_stretching=False):
    lookup = {}
    hashes = {}
    counter = 0
    g = get_hash_generator(salt, key_stretching)

    for i in range(1000):
        h = next(g)
        hashes[i] = h
        ch5 = get_hash_repeated_char(h, 5)
        if ch5:
            lookup[i] = ch5

    while True:
        lookup.pop(counter, None)
        h = next(g)
        hashes[counter + 1000] = h
        ch5 = get_hash_repeated_char(h, 5)
        if ch5:
            lookup[counter + 1000] = ch5
        yield hashes.pop(counter), lookup
        counter += 1


def key_generator(salt, key_stretching=False):
    lookups = ahead_lookup_generator(salt, key_stretching)
    counter = 0

    for h, lookup in lookups:
        ch3 = get_hash_repeated_char(h, 3)
        if ch3 and ch3 in set(lookup.values()):
            yield counter
        counter += 1


def solve(salt, counter, key_stretching=False):
    g = key_generator(salt, key_stretching)
    for i in range(counter):
        key = next(g)
    return key


if __name__ == '__main__':
    result = solve('ngcjuoqr', 64)
    print(f'Example1: {result}')

    result = solve('ngcjuoqr', 64, True)
    print(f'Example2: {result}')
