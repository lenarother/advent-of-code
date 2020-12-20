"""Day 8

https://adventofcode.com/2020/day/8

"""
from copy import deepcopy

CHANGE = {
    'nop': 'jmp',
    'jmp': 'nop',
}


def parse_input(filename):
    result = {}
    for counter, l in enumerate(open(filename).read().strip().split('\n')):
        v = l.split()
        result[counter] = (v[0], int(v[1]))
    return result


def exec_command(num, data, accumulator):
    if num not in data:
        return None, accumulator
    elif data[num][0] == 'nop':
        return num + 1, accumulator
    elif data[num][0] == 'acc':
        accumulator += data[num][1]
        return num + 1, accumulator
    elif data[num][0] == 'jmp':
        return num + data[num][1], accumulator


def run(data):
    accumulator = 0
    executed = {0: True}
    current = 0
    while True:
        past = current
        current, accumulator = exec_command(current, data, accumulator)
        if current in executed:
            return False, accumulator
        elif current is None:
            return True, accumulator
        else:
            executed[current] = True


def get_new_index_to_changed(data, changed):
    # Part 2
    for k in sorted(data.keys()):
        if changed < k and data[k][0] in CHANGE:
            return k


def check_single_dataset_(data, changed=-1):
    # Part 2
    changed = get_new_index_to_changed(data, changed)
    data[changed] = (CHANGE[data[changed][0]], data[changed][1])
    terminated, accumulator = run(data)
    return terminated, accumulator, changed


def check_all_data(data):
    # Part 2
    changed = -1
    while changed < len(data):
        copy_data = deepcopy(data)
        terminated, accumulator, changed = check_single_dataset_(copy_data, changed)
        if terminated:
            return accumulator


if __name__ =='__main__':
    # Parse input
    input1 = parse_input('inputdata/day-08-1.txt')
    input2 = parse_input('inputdata/day-08-2.txt')

    # Part 1
    result = run(input1)
    print('Part 1 - Test set 1: ', result)

    result = run(input2)
    print('Part 1 - Result: ', result)

    # Part 2
    result = check_all_data(input1)
    print('Part 2 - Test set 1: ', result)

    result = check_all_data(input2)
    print('Part 2 - Result: ', result)
