"""Day 6: Signals and Noise

https://adventofcode.com/2016/day/7

All you need to do is figure out which character
is most frequent for each position.
"""
from collections import Counter


def filter_noise(noise):
    result = ''
    rows = noise.split('\n')
    for column in zip(*rows):
        letters = Counter(column)
        result += letters.most_common()[0][0]
    return result


def filter_modified_noise(noise):
    result = ''
    rows = noise.split('\n')
    for column in zip(*rows):
        letters = Counter(column)
        result += letters.most_common()[-1][0]
    return result


if __name__ == '__main__':
    message = open('input_data.txt').read()
    print(f'Example1: {filter_noise(message)}')
    print(f'Example2: {filter_modified_noise(message)}')
