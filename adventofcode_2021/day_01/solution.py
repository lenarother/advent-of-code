"""Day 1: Sonar Sweep

https://adventofcode.com/2021/day/1

"""


def parse_data(data):
    data = data.split('\n')
    return list(map(int, data))


def get_sum(int_list, i, w):
    return sum(int_list[i:i + w])


def solve(int_list, w=1):
    increase_count = 0
    for i in range(len(int_list)):
        if (
                i < len(int_list) - w
                and get_sum(int_list, i, w) < get_sum(int_list, i + 1, w)
        ):
            increase_count += 1
    return increase_count


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    data = parse_data(input_data)

    result = solve(data)
    print(f'Example1: {result}')

    result = solve(data, 3)
    print(f'Example2: {result}')
