"""Day 1: Inverse Captcha

https://adventofcode.com/2017/day/1

"""


def get_shifted_list(data, n):
    return list(data[n:]) + list(data[:n])


def calculate_sum(l1, l2):
    return sum([
        int(x)
        for x, y in zip(l1, l2)
        if x == y
    ])


def solve(data, n=1):
    return calculate_sum(
        data,
        get_shifted_list(data, n)
    )


def solve2(data):
    return solve(data, n=int(len(data) / 2))


if __name__ == '__main__':
    input_data = open('input_data.txt').read().strip()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example1: {result}')
