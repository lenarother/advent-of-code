"""Day 7: Bridge Repair

https://adventofcode.com/2024/day/7

"""
from itertools import product

def read_input(data):
    result = {}
    for line in data.strip().split('\n'):
        line_sum, line_values = line.split(': ')
        result[int(line_sum)] = [i for i in line_values.split()]
    return result

def get_operators(n):
    return product("+*", repeat=5)

def check_equation(k, v):
    n = len(v) - 1
    foo = list(product("+*", repeat=n))
    for operator_list in foo:
        from copy import copy
        myv = copy(v)
        operator_list = list(operator_list)
        first = myv.pop(0)
        while myv:
            my = myv.pop(0)
            op = operator_list.pop(0)
            foo = f'{first}{op}{my}'
            first = eval(foo)
        if first == k:
            return k
    return 0

def solve(data):
    data = read_input(data)
    return sum([check_equation(k, v) for k, v in data.items()])


def check_equation_other(k, v):
    n = len(v) - 1
    foo = list(product("+*|", repeat=n))
    for operator_list in foo:
        from copy import copy
        myv = copy(v)
        operator_list = list(operator_list)
        first = myv.pop(0)
        while myv:
            my = myv.pop(0)
            op = operator_list.pop(0)
            if op == '|':
                first = int(f'{first}{my}')
            else:
                foo = f'{first}{op}{my}'
                first = eval(foo)

        if first == k:
            return k
    return 0

def solve2(data):
    data = read_input(data)
    incorrect_ones = {}
    result = 0
    for k, v in data.items():
        equation_result = check_equation(k, v)
        result += equation_result
        if equation_result == 0:
            incorrect_ones[k] = v
    for k, v in incorrect_ones.items():
        equation_result = check_equation_other(k, v)
        result += equation_result
    return result





if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
    result = solve2(input_data)
    print(f'Example2: {result}')