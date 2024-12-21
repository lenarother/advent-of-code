"""Day 19: Linen Layout

https://adventofcode.com/2024/day/19

"""
import re

PATTERN = r'^(r|wr|b|g|bwu|rb|gb|br)'


def get_patterns(data):
    return data.strip().split('\n\n')[0].split(', ')


def get_towels(data):
    return data.strip().split('\n\n')[1].split('\n')


def is_towel_possible(towel, patterns):
    stack = [towel]
    done = dict()
    while stack:
        current = stack.pop()
        if current == '':
            return True
        elif current in done:
            stack.append(done[current])
        else:
            for pattern in patterns:
                if current.startswith(pattern):
                    foo = len(pattern)
                    bar = current[foo:]
                    stack.append(bar)
                    done[current]= bar
    return False


def is_towel_possible_recursive(towel, patterns):
    if towel:
        for pattern in patterns:
            if towel.startswith(pattern):
                new_towel = towel[len(pattern):]
                if is_towel_possible(new_towel, patterns):
                    return True
        return False
    return True


def is_towel_possible_2(towel, patterns):
    print('pattern',list(re.finditer(PATTERN, towel)))
    counter = 0
    stack = [towel]
    done = dict()
    while stack:
        print(done)
        current = stack.pop()
        if current == '':
            counter += 1
        elif current in done:
            for i in done[current]:
                stack.append(i)
        else:
            for pattern in patterns:
                if current.startswith(pattern):
                    foo = len(pattern)
                    bar = current[foo:]
                    stack.append(bar)
                    done[current] = bar
    return counter


def solve(data):
    towels = get_towels(data)
    patterns = get_patterns(data)
    counter = 0
    for towel in towels:
        counter += is_towel_possible(towel, patterns)
    return counter


def solve2(data):
    towels = get_towels(data)
    patterns = get_patterns(data)
    counter = 0

    for i, towel in enumerate(towels):
        print(i)
        counter += is_towel_possible_2(towel, patterns)
    return counter


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
