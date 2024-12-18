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
    return [int(i) for i in data.strip().split('\n\n')[1].replace('Program: ', '').split(',')]


def literal(operand):
    return operand


def combo(operand, register):
    if operand in range(0,4):
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


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
