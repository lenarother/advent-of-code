"""Day 25: Code Chronicle

https://adventofcode.com/2024/day/25

"""


def parse_keys_and_locks(data):
    """
    The keys have the top row empty (.).
    The locks have the top row filled (#).
    """
    keys = []
    locks = []
    for keylock in data.strip().split('\n\n'):
        matrix = []
        for row in keylock.strip().split('\n'):
            matrix.append([el for el in row])
        t_matrix = zip(*matrix)  # transpose
        result = []
        for row in t_matrix:
            result.append(row.count('#') - 1)
        if matrix[0][0] == '.':
            keys.append(result)
        elif matrix[0][0] == '#':
            locks.append(result)
    return keys, locks


def is_matching(key, lock):
    return all(k + l <= 5 for k, l in zip(key, lock))


def solve(data):
    counter = 0
    keys, locks = parse_keys_and_locks(data)
    for key in keys:
        for lock in locks:
            counter += is_matching(key, lock)
    return counter


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
