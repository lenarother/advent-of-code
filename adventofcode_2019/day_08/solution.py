"""Day 8: Space Image Format

https://adventofcode.com/2019/day/8

"""


def solve(data, x, y):
    layer = ''
    size = x * y
    count_0 = size + 1
    for start in range(0, len(data), size):
        current_layer = data[start: start + size]
        current_count_0 = current_layer.count('0')
        if current_count_0 < count_0:
            layer = current_layer
            count_0 = current_count_0
    return layer.count('1') * layer.count('2')


def solve_2(data, x, y):
    size = x * y
    result = ''
    layers = [data[start: start + size] for start in range(0, len(data), size)]

    for position in range(size):
        for layer in layers:
            if layer[position] in "01":
                result += layer[position]
                break

    result = result.replace('0', '.').replace('1', '#')

    for i in range(0, len(result), x):
        print(result[i: i + x])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 25, 6)
    print(f'Example1: {result}')

    result_2 = solve_2(input_data, 25, 6)
