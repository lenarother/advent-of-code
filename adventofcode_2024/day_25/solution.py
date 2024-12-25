"""Day 25: Code Chronicle

https://adventofcode.com/2024/day/25

"""
def parse_keylocks(data):
    """
    The keys have the top row empty (.)
    The locks have the top row filled (#)
    """
    keys = []
    locks = []
    is_key = False
    is_lock = False
    for keylock in data.strip().split('\n\n'):
        if keylock[0] == '#':
            is_key = False
            is_lock = True
        elif keylock[0] == '.':
            is_key = True
            is_lock = False
        matrix = []
        for row in keylock.strip().split('\n'):
            matrix.append([el for el in row])
        t_matrix = zip(*matrix)
        result = []
        for row in t_matrix:
            result.append(row.count('#') - 1)
        if is_key:
            keys.append(result)
        elif is_lock:
            locks.append(result)
    return keys, locks


def is_matching(key, lock):
    return all(k + l <= 5 for k, l in zip(key, lock))

def solve(data):
    counter = 0
    keys, locks = parse_keylocks(data)
    for k in keys:
        for  l in locks:
            counter +=is_matching(k, l)
    return counter


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
