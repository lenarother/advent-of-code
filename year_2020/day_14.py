"""Day 14

https://adventofcode.com/2020/day/14

"""

import itertools
import operator
from functools import reduce


def parse_input(file_name):
    # Part 1
    # {location: [(bitmask, num), (bitmask, num), ...]}
    # E.g.
    # {
    #     7: [
    #        ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 101),
    #     ],
    #      8: [
    #         ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11),
    #         ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 0),
    #     ],
    # }
    result = {}
    data = open(file_name).read()
    data = data.split('mask = ')
    for item in data:
        item = item.split('\n')
        mask = item[0]
        for operation in item[1:]:
            if operation.startswith('mem'):
                operation_k, operation_v = operation.split(' = ')
                operation_k = int(operation_k.replace('mem[', '').replace(']', ''))
                operation_v = int(operation_v)
                result.setdefault(operation_k, [])
                result[operation_k].append((mask, operation_v))
    return result


def get_mem_value(decimal, mask):
    # Part 1
    binary = f'{decimal:>036b}'
    binary_with_mask = ''.join([b if m=='X' else m for b, m in zip(binary, mask)])
    return int(binary_with_mask, 2)


def calculate_memory_sum(memory_dict):
    # Part 1
    result = 0
    for mem in memory_dict:
        item = memory_dict[mem][-1]
        result += get_mem_value(item[1], item[0])
    return result


# Part 2
memory_part2 = {}


def initialize_addresses(decimal, mask, val):
    # Part 2
    binary = f'{decimal:>036b}'

    result = ''
    for b, m in zip(binary, mask):
        if m == '0':
            result += b
        else:
            result += m

    floating_count = result.count('X')
    result_divided = result.split('X')
    perms = itertools.product([0, 1], repeat=floating_count)
    for perm in perms:
        perm_to_insert = list(map(str, perm)) + ['']
        address = ''.join(reduce(operator.add, zip(result_divided, perm_to_insert)))
        memory_part2[address] = val


def initialize_memory(file_name):
    # Part 2
    data = open(file_name).read()
    data = data.split('mask = ')
    for item in data:
        item = item.split('\n')
        mask = item[0]
        for operation in item[1:]:
            if operation.startswith('mem'):
                operation_k, operation_v = operation.split(' = ')
                operation_k = int(operation_k.replace('mem[', '').replace(']', ''))
                initialize_addresses(operation_k, mask, int(operation_v))


if __name__ =='__main__':

    # Parse input
    input1 = parse_input('inputdata/day-14-1.txt')
    input2 = parse_input('inputdata/day-14-2.txt')

    # Part 1
    result = calculate_memory_sum(input1)
    print('Part 1 - Test set 1: ', result)

    result = calculate_memory_sum(input2)
    print('Part 1 - Result: ', result)

    # Part 2
    initialize_memory('inputdata/day-14-2.txt')
    result = sum(memory_part2.values())
    print('Part 2 - Result: ', result)
