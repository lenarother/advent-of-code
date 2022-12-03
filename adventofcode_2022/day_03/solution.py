"""Day 3: Rucksack Reorganization

https://adventofcode.com/2022/day/3

"""
from string import ascii_lowercase, ascii_uppercase

LETTERS = list(ascii_lowercase)
LETTERS_UPPERCASE = list(ascii_uppercase)


def get_item_type(data):
    n = int(len(data)/2)
    compartment1 = set(data[:n])
    compartment2 = set(data[n:])
    return compartment1.intersection(compartment2).pop()


def get_priority(item_type):
    if item_type.isupper():
        return 26 + 1 + LETTERS_UPPERCASE.index(item_type)
    return 1 + LETTERS.index(item_type)


def get_badge_type(a, b, c):
    return set(c).intersection(set(a).intersection(set(b))).pop()


def solve(data):
    return sum([
        get_priority(get_item_type(i))
        for i in data.strip().split('\n')
    ])


def groups(data):
    data = data.strip().split('\n')
    for i in range(int(len(data)/3)):
        n = i * 3
        yield data[n], data[n+1], data[n+2]


def solve2(data):
    return sum([
        get_priority(get_badge_type(*group))
        for group in groups(data)
    ])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
