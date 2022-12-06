"""Day 6: Tuning Trouble

https://adventofcode.com/2022/day/6

"""


def solve(data, n=4):
    for i in range(len(data) - n):
        current = data[i:i+n]
        if len(set(current)) == n:
            return i + n


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, 14)
    print(f'Example2: {result}')
