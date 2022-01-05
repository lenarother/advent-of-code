"""Day 4: The Ideal Stocking Stuffer

https://adventofcode.com/2015/day/4

"""
import hashlib


def hash_counter(base, zero_count=5):
    counter = 0
    while 1:
        temp = hashlib.md5(f'{base}{counter}'.encode('utf-8')).hexdigest()
        if temp.startswith('0' * zero_count):
            yield counter
        counter += 1


def solve(base, zero_count=5):
    hash_gen = hash_counter(base, zero_count)
    i = next(hash_gen)
    return i


if __name__ == '__main__':
    result = solve('iwrupvqb')
    print(f'Example1: {result}')

    result = solve('iwrupvqb', 6)
    print(f'Example1: {result}')
