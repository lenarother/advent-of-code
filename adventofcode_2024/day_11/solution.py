"""Day 11: Plutonian Pebbles

https://adventofcode.com/2024/day/11

"""
from collections import defaultdict


def apply_rule(n):
    if n == '0':
        return ['1']
    elif len(n) % 2 == 0:
        n_len = int(len(n) / 2)
        return [str(int(n[:n_len])), str(int(n[n_len:]))]
    else:
        return [str(int(n) * 2024)]


def do_step(input_dict):
    todo_dict = defaultdict(int)
    for n, rep in input_dict.items():
        result = apply_rule(n)
        for i in result:
            todo_dict[i] += rep
    return todo_dict


def solve(data, n):
    mydata = data.strip().split()
    data_dict = defaultdict(int)
    for i in mydata:
        data_dict[i] += 1

    while n:
        data_dict = do_step(data_dict)
        n -= 1

    return sum(data_dict.values())


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data, 25)
    print(f'Example1: {result}')

    result = solve(input_data, 75)
    print(f'Example1: {result}')
