"""Day 16: Permutation Promenade

https://adventofcode.com/2017/day/16

"""
import re

MOVE_SPIN = re.compile(r's(\d+)')
MOVE_SWAP_BY_POSITION = re.compile(r'x(\d+)/(\d+)')
MOVE_SWAP_BY_NAME = re.compile(r'p(\w)/(\w)')


def dance(seq, moves):
    seq = list(seq)

    for move in moves.split(','):
        if MOVE_SPIN.match(move):
            n = -1 * int(MOVE_SPIN.findall(move)[0])
            seq = seq[n:] + seq[:n]
        elif MOVE_SWAP_BY_POSITION.match(move):
            x, y = list(map(int, (MOVE_SWAP_BY_POSITION.findall(move)[0])))
            seq[x], seq[y] = seq[y], seq[x]
        elif MOVE_SWAP_BY_NAME.match(move):
            a, b = MOVE_SWAP_BY_NAME.findall(move)[0]
            x, y = seq.index(a), seq.index(b)
            seq[x], seq[y] = seq[y], seq[x]

    return ''.join(seq)


def find_repetition_cycle_size(moves, seq='abcdefghijklmnop'):
    original_seq = seq
    i = 1
    seq = dance(seq, moves)
    while seq != original_seq:
        seq = dance(seq, moves)
        i += 1
    return i


def solve(moves, seq='abcdefghijklmnop', i=1):
    repetition_cycle_size = find_repetition_cycle_size(moves, seq)
    i = i % repetition_cycle_size
    while i:
        seq = dance(seq, moves)
        i -= 1
    return seq


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(moves=input_data)
    print(f'Example1: {result}')

    result = solve(moves=input_data, i=1_000_000_000)
    print(f'Example2: {result}')
