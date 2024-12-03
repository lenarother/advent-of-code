"""Day 3: Mull It Over

https://adventofcode.com/2024/day/3

"""
import re


def solve(data):
    result = 0
    for i in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data):
        expr = (eval(i.replace('mul', '')))
        result += expr[0] * expr[1]
    return result


def solve2(data):
    result = 0
    enabled = True
    for i in re.findall(
            r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)",
            data
    ):
        if i.startswith('don'):
            enabled = False
        elif i.startswith('do'):
            enabled = True
        elif i.startswith('mul') and enabled is True:
            expr = (eval(i.replace('mul', '')))
            result += expr[0] * expr[1]
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
