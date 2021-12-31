"""Day 1: Sonar Sweep

https://adventofcode.com/2021/day/1

"""


def parse_data(data):
    return list(map(int, data.split('\n')))


def solve(int_list, w=1):
    return sum([
        int_list[i] < int_list[i + w]
        for i in range(len(int_list) - w)
    ])


if __name__ == '__main__':
    input_data = parse_data(open('input_data.txt').read())

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, 3)
    print(f'Example2: {result}')
