"""Day 20: Grove Positioning System

https://adventofcode.com/2022/day/20

"""

class MovableInt(int):
    moved = False


def parse(data):
    # Attention len(data) != len(set(data))
    for n in map(int, data.strip().split('\n')):
        yield MovableInt(n)


def get_new_index(n, current_index):
    return n + current_index


def move_number(n, result):
    current_index = result.index(n)
    while result[current_index].moved:
        current_index = result.index(n, current_index)
    new_index = get_new_index(n, current_index)
    # result[current_index], result[new_index] = result[new_index], result[current_index]
    # remove
    result = result[:current_index] + result[current_index + 1:]
    n.moved = True
    result = result[:new_index] + [n] + result[new_index:]
    return result


def solve(data):
    result = list(parse(data))
    for n in parse(data):
        result = move_number(n, result)


    return result






if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
