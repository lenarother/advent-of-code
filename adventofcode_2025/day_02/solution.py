"""Day 2: Gift Shop

https://adventofcode.com/2025/day/2

"""


def is_id_valid(id):
    id = str(id)
    if len(id) % 2 == 1:
        return True
    my_len = len(id) // 2
    if id[:my_len] == id[my_len:]:
        return False
    return True


def is_id_valid_2(id):
    id = str(id)
    if len(id) < 2:
        return True
    for n in range(1, (len(id) // 2) + 1):
        if len(id) % n == 0:
            elements = [id[i:i + n] for i in range(0, len(id), n)]
            if elements.count(elements[0]) == len(elements):
                return False
    return True


def range_iterator(range_str):
    x, y = range_str.split("-")
    for i in range(int(x), int(y) + 1):
        yield i


def solve(data, algorithm):
    result = 0
    ranges = data.strip().split(',')
    for range in ranges:
        for id in range_iterator(range):
            if not algorithm(id):
                result += int(id)
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, is_id_valid)
    print(f'Example1: {result}')
    result = solve(input_data, is_id_valid_2)
    print(f'Example2: {result}')
