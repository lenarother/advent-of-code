"""Day 1: Calorie Counting

https://adventofcode.com/2022/day/1

"""


def solve(data, n=1):
    return sum(sorted([
        sum(map(int, d.strip().split('\n')))
        for d in data.strip().split('\n\n')
    ], reverse=True)[:n])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, 3)
    print(f'Example2: {result}')
