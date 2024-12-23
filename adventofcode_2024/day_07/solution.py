"""Day 7: Bridge Repair

https://adventofcode.com/2024/day/7

"""
import operator
from copy import copy
from itertools import product


def read_input(data):
    result = {}
    for line in data.strip().split('\n'):
        line_sum, line_values = line.split(': ')
        result[int(line_sum)] = [i for i in line_values.split()]
    return result


def generate_operators(n, include_concatenation=False):
    operators = [operator.mul, operator.add]
    if include_concatenation:
        operators.append(concatenation)
    return product(operators, repeat=n)


def concatenation(x, y):
    return int(f'{x}{y}')


def check_equation(k, v, include_concatenation=False):
    n = len(v) - 1
    for operator_list in generate_operators(n, include_concatenation):
        numbers = copy(v)
        operator_list = list(operator_list)
        first = numbers.pop(0)
        while numbers:
            second = numbers.pop(0)
            current_operator = operator_list.pop(0)
            first = current_operator(int(first), int(second))
        if first == k:
            return k
    return 0


def solve(data):
    data = read_input(data)
    return sum([check_equation(k, v) for k, v in data.items()])


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
        equation_result = check_equation(k, v, include_concatenation=True)
        result += equation_result
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
