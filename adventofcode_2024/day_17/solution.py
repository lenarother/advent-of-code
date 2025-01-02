"""Day 17: Chronospatial Computer

https://adventofcode.com/2024/day/17

"""
import re


def get_register(data):
    return {
        'A': int(re.findall(r'Register A: (\d+)', data)[0]),
        'B': int(re.findall(r'Register B: (\d+)', data)[0]),
        'C': int(re.findall(r'Register C: (\d+)', data)[0]),
    }


def get_program(data):
    data = data.strip().split('\n\n')
    return [int(i) for i in data[1].replace('Program: ', '').split(',')]


def literal(operand):
    return operand


def combo(operand, register):
    if operand in range(4):
        return operand
    elif operand == 4:
        return register['A']
    elif operand == 5:
        return register['B']
    elif operand == 6:
        return register['C']
    elif operand == 7:
        raise InterruptedError


def instruction(opcode, operand, register, instruction_pointer):
    # adv
    if opcode == 0:
        register['A'] = int(register['A'] / (2 ** combo(operand, register)))

    # bxl
    elif opcode == 1:
        register['B'] = register['B'] ^ literal(operand)

    # bst
    elif opcode == 2:
        register['B'] = int(str((combo(operand, register) % 8))[-3:])

    # jnz
    elif opcode == 3:
        if register['A'] == 0:
            pass
        else:
            return None, literal(operand)
    # bxc
    elif opcode == 4:
        register['B'] = register['B'] ^ register['C']

    # out
    elif opcode == 5:
        return combo(operand, register) % 8, instruction_pointer + 2

    # bdv
    if opcode == 6:
        register['B'] = int(register['A'] / (2 ** combo(operand, register)))

    # cdv
    if opcode == 7:
        register['C'] = int(register['A'] / (2 ** combo(operand, register)))

    return None, instruction_pointer + 2


def solve(data):
    register = get_register(data)
    program = get_program(data)
    instruction_pointer = 0
    outputs = []
    while instruction_pointer < len(program):
        val, instruction_pointer = instruction(
            program[instruction_pointer],
            program[instruction_pointer + 1],
            register,
            instruction_pointer
        )
        if val is not None:
            outputs.append(val)

    result = ','.join([str(i) for i in outputs])
    return result


def get_possible_input():
    from itertools import product
    for i in product('01', repeat=3):
        yield i


def run_algorithm(a):
    """Translated to Python algorithm from puzzle input."""
    result = []
    while a:                # jnz
        b = a % 8           # bst
        b = b ^ 1           # bxl
        c = a // (2 ** b)   # cdv
        a = a // 8          # adv
        b = b ^ c           # bxc
        b = b ^ 6           # bxl
        result.append(b % 8)        # out
    return result


def solve2(data):
    expected = [0, 3, 5, 5, 6, 1, 7, 4, 3, 0, 5, 7, 1, 1, 4, 2]
    results = ['']

    while True:
        new_results = []
        for result in results:
            for i in get_possible_input():
                to_try = result + ''.join(i)
                a = int(to_try, 2)
                output = run_algorithm(a)

                if list(reversed(output)) == expected:
                    return a

                if list(reversed(output)) == expected[:int(len(to_try) / 3)]:
                    new_results.append(to_try)

        results = new_results


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
