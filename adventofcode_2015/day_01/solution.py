"""Day 1: Not Quite Lisp

https://adventofcode.com/2015/day/1

"""


def solve(data):
    return data.count('(') - data.count(')')


def solve2(data):
    floor = 0
    for i, ch in enumerate(data.strip()):
        floor += 1 if ch == '(' else -1 if ch == ')' else 0
        if floor == -1:
            return i + 1


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
