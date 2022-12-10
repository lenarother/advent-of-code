"""Day 10: Cathode-Ray Tube

https://adventofcode.com/2022/day/10

"""


def data_gen(data):
    for line in data.strip().split('\n'):
        line = line.split()
        if len(line) == 1:
            yield line[0], None
        else:
            yield line[0], int(line[1])


def device_cycle(data):
    register = 1
    cycle_time = 1
    for instruction, value in data_gen(data):
        if instruction == 'noop':
            yield cycle_time, register
            cycle_time += 1
        if instruction == 'addx':
            yield cycle_time, register
            cycle_time += 1
            yield cycle_time, register
            register += value
            cycle_time += 1


def solve(data):
    values = {cycle_time: value for cycle_time, value in device_cycle(data)}
    return sum([(values[i] * i) for i in [20, 60, 100, 140, 180, 220]])


def solve2(data):
    screen = ''

    for k, v in device_cycle(data):
        sprite = [v-1, v, v+1]
        position = (k - 1) % 40
        screen += '#' if position in sprite else '.'
        if k % 40 == 0:
            screen += '\n'

    return screen


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    print(solve2(input_data))
