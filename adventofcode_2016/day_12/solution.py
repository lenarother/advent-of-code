"""Day 12: Leonardo's Monorail

https://adventofcode.com/2016/day/12

"""
import re
from collections import OrderedDict

CPY = r'cpy (-?)(\d+|[abcd]) ([abcd])'
INC = r'inc ([abcd])'
DEC = r'dec ([abcd])'
JNZ = r'jnz (\d+|[abcd]) (-?)(\d+)'


def update_value(instruction, values):
    for s, v, ch in re.findall(CPY, instruction):
        values[ch] = (
            values[v] if not v.isnumeric()
            else int(v) * (-1 if s else 1)
        )
    for ch in re.findall(INC, instruction):
        values[ch] += 1
    for ch in re.findall(DEC, instruction):
        values[ch] -= 1


def jnz(instruction, values):
    for check, sign, jump in re.findall(JNZ, instruction):
        check_value = int(check) if check.isnumeric() else values[check]
        if check_value != 0:
            return int(jump) * (-1 if sign else 1)
    return 1


def solve(data, initial_values=None):
    values = initial_values or OrderedDict({
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0
    })

    instructions = data.split('\n')
    counter = 0
    while counter < len(instructions):
        update_value(instructions[counter], values)
        counter += jnz(instructions[counter], values)
    return tuple(values.values())


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    values = OrderedDict({
        'a': 0,
        'b': 0,
        'c': 1,
        'd': 0
    })
    result = solve(input_data, values)
    print(f'Example1: {result}')
