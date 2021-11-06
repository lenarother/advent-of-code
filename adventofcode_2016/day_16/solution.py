"""Day 16: Dragon Checksum

https://adventofcode.com/2016/day/16

"""
from collections import deque


def get_reverse_state(initial_state):
    return ''.join(
        map(
            lambda i: '1' if i == '0' else '0',
            reversed(list(initial_state))
        )
    )


def get_data(initial_state, disc_size):
    data = initial_state
    while len(data) < disc_size:
        data = f'{data}0{get_reverse_state(data)}'
    return data[:disc_size]


def get_checksum(data):
    data = deque(list(data))
    checksum = ''
    while data:
        i, j = int(data.popleft()), int(data.popleft())
        checksum += str(int(i == j))
    return checksum


def get_odd_checksum(checksum):
    while True:
        checksum = get_checksum(checksum)
        if len(checksum) % 2 == 1:
            return checksum


def solve(initial_state, disc_size):
    data = get_data(initial_state, disc_size)
    return get_odd_checksum(data)


if __name__ == '__main__':
    result = solve('10111011111001111', 272)
    print(f'Example1: {result}')

    result = solve('10111011111001111', 35651584)
    print(f'Example2: {result}')
