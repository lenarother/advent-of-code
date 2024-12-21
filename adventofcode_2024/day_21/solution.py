"""Day 21: Keypad Conundrum

https://adventofcode.com/2024/day/21

"""
import heapq
from itertools import permutations

#+---+---+---+
#| 7 | 8 | 9 |
#+---+---+---+
#| 4 | 5 | 6 |
#+---+---+---+
#| 1 | 2 | 3 |
#+---+---+---+
#    | 0 | A |
#    +---+---+


NUMERIC_KEYBOARD_MOVES = {
    # 0
    ('0', 'A'): '>',
    ('0', '1'): '^<', # f '<^'
    ('0', '2'): '^',
    ('0', '3'): '^>',
    ('0', '4'): '^^<', # f '<^^'
    ('0', '5'): '^^',
    ('0', '6'): '^^>',
    ('0', '7'): '^^^<', # '<^^^'
    ('0', '8'): '^^^',
    ('0', '9'): '^^^>',

    # 1
    ('1', 'A'): '>>v', # f 'v>>'
    ('1', '0'): '>v', # f 'v>'
    ('1', '2'): '>',
    ('1', '3'): '>>',
    ('1', '4'): '^',
    ('1', '5'): '>^',
    ('1', '6'): '>>^',
    ('1', '7'): '^^',
    ('1', '8'): '^^>',
    ('1', '9'): '^^>>',

    # 2
    ('2', 'A'): '>v',
    ('2', '0'): 'v',
    ('2', '1'): '<',
    ('2', '3'): '>',
    ('2', '4'): '^<',
    ('2', '5'): '^',
    ('2', '6'): '^>',
    ('2', '7'): '^^<',
    ('2', '8'): '^^',
    ('2', '9'): '^^>',

    # 3
    ('3', 'A'): 'v',
    ('3', '0'): 'v<',
    ('3', '1'): '<<',
    ('3', '2'): '<',
    ('3', '4'): '^<<',
    ('3', '5'): '^<',
    ('3', '6'): '^',
    ('3', '7'): '<<^^',
    ('3', '8'): '^^<',
    ('3', '9'): '^^',

    # 4
    ('4', 'A'): '>>vv', # f 'vv>>'
    ('4', '0'): '>vv', # f 'vv>'
    ('4', '1'): 'v',
    ('4', '2'): '>v',
    ('4', '3'): '>>v',
    ('4', '5'): '>',
    ('4', '6'): '>>',
    ('4', '7'): '^',
    ('4', '8'): '^>',
    ('4', '9'): '^>>',

    # 5
    ('5', 'A'): '>vv',
    ('5', '0'): 'vv',
    ('5', '1'): 'v<',
    ('5', '2'): 'v',
    ('5', '3'): '>v',
    ('5', '4'): '<',
    ('5', '6'): '>',
    ('5', '7'): '^<',
    ('5', '8'): '^',
    ('5', '9'): '^>',

    # 6
    ('6', 'A'): 'vv',
    ('6', '0'): 'vv<',
    ('6', '1'): 'v<<',
    ('6', '2'): 'v<',
    ('6', '3'): 'v',
    ('6', '4'): '<<',
    ('6', '5'): '<',
    ('6', '7'): '^<<',
    ('6', '8'): '^<',
    ('6', '9'): '^',

    # 7
    ('7', 'A'): '>>vvv', # f 'vvv>>'
    ('7', '0'): '>vvv', # f 'vvv>'
    ('7', '1'): 'vv',
    ('7', '2'): '>vv',
    ('7', '3'): '>>vv',
    ('7', '4'): 'v',
    ('7', '5'): '>v',
    ('7', '6'): '>>v',
    ('7', '8'): '>',
    ('7', '9'): '>>',

    # 8
    ('8', 'A'): '>vvv',
    ('8', '0'): 'vvv',
    ('8', '1'): 'vv<',
    ('8', '2'): 'vv',
    ('8', '3'): 'vv>',
    ('8', '4'): 'v<',
    ('8', '5'): 'v',
    ('8', '6'): 'v>',
    ('8', '7'): '<',
    ('8', '9'): '>',

    # 9
    ('9', 'A'): 'vvv',
    ('9', '0'): 'vvv<',
    ('9', '1'): 'vv<<',
    ('9', '2'): 'vv<',
    ('9', '3'): 'vv',
    ('9', '4'): 'v<<',
    ('9', '5'): 'v<',
    ('9', '6'): 'v',
    ('9', '7'): '<<',
    ('9', '8'): '<',

    # A
    ('A', '0'): '<',
    ('A', '1'): '^<<', # f '<<^'
    ('A', '2'): '^<',
    ('A', '3'): '^',
    ('A', '4'): '^^<<', # '<<^^'
    ('A', '5'): '^^<',
    ('A', '6'): '^^',
    ('A', '7'): '^^^<<', # '<<^^^
    ('A', '8'): '^^^<',
    ('A', '9'): '^^^',
}


DIRECTIONAL_KEYBOARD_MOVES = {
    # A
    ('A', '^'): '<',
    ('A', '<'): 'v<<',
    ('A', '>'): 'v',
    ('A', 'v'): 'v<',

    # ^
    ('^', 'A'): '>',
    ('^', '<'): 'v<',
    ('^', '>'): 'v>',
    ('^', 'v'): 'v',

    # v
    ('v', 'A'): '^>',
    ('v', '<'): '<',
    ('v', '>'): '>',
    ('v', '^'): '^',

    # <
    ('<', 'A'): '>>^',
    ('<', 'v'): '>',
    ('<', '>'): '>>',
    ('<', '^'): '>^',

    # >
    ('>', 'A'): '^',
    ('>', 'v'): '<',
    ('>', '<'): '<<',
    ('>', '^'): '<^',
}

FORBIDDEN = {
    ('0', '1'): '<^',
    ('0', '4'): '<^^',
    ('0', '7'): '<^^^',
    ('1', 'A'): 'v>>',
    ('1', '0'): 'v>',
    ('4', 'A'): 'vv>>',
    ('4', '0'): 'vv>',
    ('7', 'A'): 'vvv>>',
    ('7', '0'): 'vvv>',
    ('A', '1'): '<<^',
    ('A', '4'): '<<^^',
    ('A', '7'): '<<^^^',
}


def optimise_numeric_keypad():
    from itertools import permutations
    result = dict()

    for k, v in NUMERIC_KEYBOARD_MOVES.items():
        best = 1000000
        best_path = ''
        for perm in permutations(v, len(v)):
            path = ''.join(perm)
            if path != FORBIDDEN.get(k):
                foo = get_directional_code_path(path)
                foo = get_directional_code_path(foo)
                if len(foo) < best:
                    best_path = path
                    best = len(foo)
        result[k] = best_path
    return result


def get_numeric_code_path(code='029A', keypad=NUMERIC_KEYBOARD_MOVES):
    code = f'A{code}'
    path = ''
    for i, j in zip(code[:-1], code[1:]):
        if i != j:
            path += keypad[(i, j)]
        path += 'A'
    return path


def get_directional_code_path(code='<A^A>^^AvvvA'):
    code = f'A{code}'
    path = ''
    for i, j in zip(code[:-1], code[1:]):
        if i != j:
            path += DIRECTIONAL_KEYBOARD_MOVES[(i, j)]
        path += 'A'
    return path


def get_path_value(code):
    keypad = optimise_numeric_keypad()
    result_code = get_numeric_code_path(code, keypad)
    result_code = get_directional_code_path(result_code)
    result_code = get_directional_code_path(result_code)
    return int(code.replace('A', '')) * len(result_code)




def solve(data):
    data = data.strip().split('\n')
    return sum([get_path_value(code) for code in data])



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
