"""Day 21: Scrambled Letters and Hash

https://adventofcode.com/2016/day/21

"""
import re

SWAP = r'swap (letter|position) (\w+) with (letter|position) (\w+)'
ROTATE = r'rotate (right|left) (\d+) steps?'
ROTATE_BASED = r'rotate based on position of letter ([a-z])'
REVERSE = r'reverse positions (\d+) through (\d+)'
MOVE = r'move position (\d+) to position (\d+)'

ROTATE_BASED_MOVES = {
    # current_position: left_rotation
    1: 1,
    3: 2,
    5: 3,
    7: 4,
    2: 6,
    4: 7,
    6: 8,
    0: 9,
}


def swap(psw_list, p1, p2):
    psw_list[p1], psw_list[p2] = psw_list[p2], psw_list[p1]
    return ''.join(psw_list)


def swap_instruction(psw, rule):
    psw = list(psw)
    mode, p1, _, p2 = re.findall(SWAP, rule)[0]

    if mode == 'position':
        return swap(psw, int(p1), int(p2))

    p1 = psw.index(p1)
    p2 = psw.index(p2)
    return swap(psw, p1, p2)


def rotate(psw, p):
    return f'{psw[p:]}{psw[:p]}'


def rotate_instruction(psw, rule, reverse):
    direction, p = re.findall(ROTATE, rule)[0]
    p = (int(p) % len(psw)) * (-1 if direction == 'right' else 1)
    p = p * (-1 if reverse else 1)
    return rotate(psw, p)


def rotate_based_instruction(psw, rule, reverse):
    ch = re.findall(ROTATE_BASED, rule)[0]
    list_psw = list(psw)
    if not reverse:
        p = list_psw.index(ch)
        p += 2 if p >= 4 else 1
        p = (p % len(psw)) * -1
    elif reverse:
        if len(psw) != 8:
            raise Exception('Cannot reverse rotation!')
        chp = list_psw.index(ch)
        p = ROTATE_BASED_MOVES[chp]
    return rotate(psw, p)


def reverse_instruction(psw, rule, reverse):
    p1, p2 = map(int, re.findall(REVERSE, rule)[0])
    return (
        f'{psw[:p1]}'
        f'{"".join(reversed(list(psw[p1:p2 + 1])))}'
        f'{psw[p2 + 1:]}'
    )


def move_instruction(psw, rule, reverse):
    p1, p2 = map(int, re.findall(MOVE, rule)[0])
    if reverse:
        p1, p2 = p2, p1
    psw_list = list(psw)
    ch = psw_list.pop(p1)
    return ''.join(psw_list[:p2] + [ch] + psw_list[p2:])


def apply_instruction(psw, instruction, reverse):
    if instruction.startswith('swap'):
        return swap_instruction(psw, instruction)
    elif instruction.startswith('rotate based'):
        return rotate_based_instruction(psw, instruction, reverse)
    elif instruction.startswith('rotate'):
        return rotate_instruction(psw, instruction, reverse)
    elif instruction.startswith('reverse'):
        return reverse_instruction(psw, instruction, reverse)
    elif instruction.startswith('move'):
        return move_instruction(psw, instruction, reverse)
    return psw


def solve(psw, instructions, reverse=False):
    instructions = instructions.split('\n')
    if reverse:
        instructions = reversed(instructions)

    for i in instructions:
        psw = apply_instruction(psw, i, reverse)
    return psw


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve('abcdefgh', input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = solve('fbgdceah', input_data, True)
    print(f'Example2: {result}')
