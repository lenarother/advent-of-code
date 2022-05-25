"""Day 9: Stream Processing

https://adventofcode.com/2017/day/9

"""
import re

GARBAGE = re.compile(r'([^<]*)(<[^>]*>)?(.*)')
NEGATION = re.compile(r'(!.)')


def remove_garbage(data):
    done = ''
    todo = data
    garbage_length = 0

    while len(todo) > 0:

        before, garbage, after = GARBAGE.findall(todo)[0]
        done += before
        garbage = re.sub(NEGATION, '', garbage)

        if garbage.endswith('>'):
            todo = after
            garbage_length += len(garbage) - 2
        else:
            todo = garbage + after

    return done, garbage_length


def calculate_score(data):
    total_score = 0
    current_score = 1

    for x in data:
        if x == '{':
            total_score += current_score
            current_score += 1
        elif x == '}':
            current_score -= 1

    return total_score


def solve(data):
    data, _ = remove_garbage(data)
    return calculate_score(data)


def solve2(data):
    _, garbage_length = remove_garbage(data)
    return garbage_length


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
