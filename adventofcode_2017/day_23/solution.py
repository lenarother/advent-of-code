"""Day 23: Coprocessor Conflagration

https://adventofcode.com/2017/day/23

"""

import re
from collections import defaultdict

INSTRUCTION_SET = re.compile(r'(\w\w\w) (\w)\s?(-?)(\d+|\w?)')


def get_val(val, sign, register):
    if not val:
        return 0
    if val.isnumeric():
        return int(val) if not sign else -1 * int(val)
    return register.get(val, 0)


def parse_instructions(instructions):
    return {
        k: v for k, v
        in enumerate(instructions.strip().split('\n'))
    }


def execute(instructions):
    instructions = parse_instructions(instructions)
    register = defaultdict(int)
    i = 0
    mul_counter = 0

    while i in instructions:
        name, var, sign, val = INSTRUCTION_SET.findall(instructions[i])[0]
        val = get_val(val, sign, register)

        if name == 'set':
            register[var] = val

        if name == 'sub':
            register[var] -= val

        elif name == 'mul':
            register[var] *= val
            mul_counter += 1

        elif name == 'jnz':
            var = get_val(var, '', register)
            if var != 0:
                i += val - 1

        i += 1
    return register, mul_counter


def solve(data):
    register, mul_counter = execute(data)
    return mul_counter


def inner(b, d, f):
    """Check if b can be divided by d"""
    e = 2
    while True:
        if d * e == b:
            f = 0
        e += 1
        if e == b:
            return f


def is_prime(b):
    d = 2
    while d < b:
        if b % d == 0:
            return False
        d += 1
    return True


def solve2():
    b = 108400
    c = b + 17000
    h = 0

    while b <= c:
        if not is_prime(b):
            h += 1
        b += 17
    return h


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2()
    print(f'Example2: {result}')
