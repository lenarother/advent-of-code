"""Day 23: Opening the Turing Lock

https://adventofcode.com/2015/day/23

"""


def execute(register_in, code):
    program = code.split('\n')
    cursor = 0

    while cursor < len(program):
        line = program[cursor]

        match line.split():
            case ['inc', register]:
                register_in[register] += 1
            case ['hlf', register]:
                val = register_in.get(register)
                if val % 2 != 0:
                    raise ValueError
                register_in[register] = val / 2
            case ['tpl', register]:
                register_in[register] *= 3
            case ['jmp', register]:
                cursor += int(register) - 1
            case ['jie', register, offset]:
                val = register_in.get(register.strip(','), register)
                offset = int(offset)
                if val % 2 == 0:
                    cursor += offset - 1
            case ['jio', register, offset]:
                val = register_in.get(register.strip(','), register)
                offset = int(offset)
                if val == 1:
                    cursor += offset - 1
        cursor += 1

    return register_in


def solve(data, a=0):
    return execute({'a': a, 'b': 0}, data)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, a=1)
    print(f'Example2: {result}')
