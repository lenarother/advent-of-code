"""Day 3: Rucksack Reorganization

https://adventofcode.com/2022/day/3

"""
from string import ascii_lowercase

LETTERS = list(ascii_lowercase)


def compartments(data):
    for i in data.strip().split('\n'):
        n = len(i) // 2
        yield i[:n], i[n:]


def groups(data):
    data = data.strip().split('\n')
    for i in range(int(len(data)/3)):
        n = i * 3
        yield data[n], data[n+1], data[n+2]


def get_common_element(*items):
    common = set(items[0]).intersection(set(items[1]))
    for i in items[2:]:
        common = common.intersection(set(i))
    return common.pop()


def get_priority(letter):
    return 1 + LETTERS.index(letter.lower()) + (26 * int(letter.isupper()))


def solve(data, item_iterator=compartments):
    return sum([
        get_priority(get_common_element(*i))
        for i in item_iterator(data)
    ])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, item_iterator=groups)
    print(f'Example2: {result}')
