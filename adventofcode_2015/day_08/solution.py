"""Day 8: Matchsticks

https://adventofcode.com/2015/day/8

"""
import sys
from io import StringIO


def count_in_memory_chars(data):
    return len(data) - 2


def count_total_chars(data):
    return len(data)


def count_in_memory_chars_from_file(filename):
    old_stdout = sys.stdout
    print_output = StringIO()
    sys.stdout = print_output

    text = ''
    f = open(filename, 'r').readlines()
    for line in f:
        text += line.strip()[1:-1]
    eval('print("' + text + '")')

    sys.stdout = old_stdout
    return len(print_output.getvalue().strip())


def count_total_chars_from_file(filename):
    f = open(filename).read()
    return len(f) - f.count('\n')


def count_total_chars_extra_raw_from_file(filename):
    count = 0
    f = open(filename).readlines()
    for line in f:
        line = line.strip()
        line = repr(line)
        line = line.replace('"', '\\"')
        count += len(line)
    return count


def solve(filename):
    total_count = count_total_chars_from_file(filename)
    in_memory_count = count_in_memory_chars_from_file(filename)
    return total_count - in_memory_count


def solve2(filename):
    total_count = count_total_chars_from_file(filename)
    raw_count = count_total_chars_extra_raw_from_file(filename)
    return raw_count - total_count


if __name__ == '__main__':
    result = solve('input_data.txt')
    print(f'Example1: {result}')

    result = solve2('input_data.txt')
    print(f'Example2: {result}')
