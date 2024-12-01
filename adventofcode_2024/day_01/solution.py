"""Day 1: Historian Hysteria

https://adventofcode.com/2024/day/1

"""


def parse_data(data):
    """
    Covers string input into two lists of ints.

    Args:
    Multiple line string with two numbers in each row.
        3   4
        4   3
        2   5

    Returns:
        [3, 4, 2], [4, 3, 5]
    """
    first_list = []
    second_list = []
    for row in data.strip().split('\n'):
        i, j = row.split()
        first_list.append(int(i))
        second_list.append(int(j))
    return first_list, second_list


def solve(data):
    first_list, second_list = parse_data(data)
    first_list.sort()
    second_list.sort()
    return sum([abs(i - j) for i, j in zip(first_list, second_list)])


def solve2(data):
    first_list, second_list = parse_data(data)
    return sum([i * second_list.count(i) for i in first_list])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
