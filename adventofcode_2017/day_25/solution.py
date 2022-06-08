"""Day 25: The Halting Problem

https://adventofcode.com/2017/day/25

"""
import re
from collections import namedtuple

STEPS_COUNT = re.compile(r'Perform a diagnostic checksum after (\d+) steps.')
STATE = re.compile(
    r"""In state (\w):
  If the current value is (0|1):
    - Write the value (0|1).
    - Move one slot to the (left|right).
    - Continue with state (\w).
  If the current value is (0|1):
    - Write the value (0|1).
    - Move one slot to the (left|right).
    - Continue with state (\w)."""
)

Operation = namedtuple('Operation', 'write move next_state')


def parse_steps_count(data):
    return int(STEPS_COUNT.findall(data)[0])


def parse_states(data):
    states = {}
    blocks = data.strip().split('\n\n')

    for b in blocks:
        if STATE.match(b):
            state = STATE.findall(b)[0]
            states[state[0]] = {
                int(state[1]): Operation(
                    int(state[2]),
                    -1 if state[3] == 'left' else 1,
                    state[4],
                ),
                int(state[5]): Operation(
                    int(state[6]),
                    -1 if state[7] == 'left' else 1,
                    state[8],
                )
            }
    return states


def solve(data):
    tape = {}
    n = parse_steps_count(data)
    states = parse_states(data)

    state = 'A'
    cursor = 0

    while n:
        current_value = tape.get(cursor, 0)
        operation = states[state][current_value]
        tape[cursor] = operation.write
        cursor += operation.move
        state = operation.next_state
        n -= 1

    return sum(tape.values())


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
