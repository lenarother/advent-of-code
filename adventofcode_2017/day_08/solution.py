"""Day 8: I Heard You Like Registers

https://adventofcode.com/2017/day/8

"""
from collections import defaultdict


def solve(data):
    register = defaultdict(int)
    max_val = 0

    for line in data.strip().split('\n'):
        instruction, condition = line.split(' if ')
        var, check, val = condition.split()

        if eval(f'{register.get(var, 0)} {check} {val}'):
            var, inst, val = instruction.split()
            register[var] += int(val) * (1 if inst == 'inc' else -1)
            max_val = max(max_val, register[var])

    return max(register.values()), max_val


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result, max_result = solve(input_data)
    print(f'Example1: {result}')
    print(f'Example2: {max_result}')
