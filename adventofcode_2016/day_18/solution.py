"""Day 18: Like a Rogue

https://adventofcode.com/2016/day/18

"""


def solve_triple(x, z):
    return '.' if x == z else '^'


def solve_row(row):
    extra_row = '.' + row + '.'
    return ''.join([
        solve_triple(x, z)
        for x, z in zip(extra_row[:-1], extra_row[2:])
    ])


def solve(row, size):
    dots_count = row.count('.')
    while size > 1:
        row = solve_row(row)
        dots_count += row.count('.')
        size -= 1
    return dots_count


# pretty but exceeds recursion depth
# def solve(row, size, result=0):
#     result += row.count('.')
#     if size > 1:
#         return solve(solve_row(row), size - 1, result)
#     return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read().strip()
    result = solve(input_data, 40)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read().strip()
    result = solve(input_data, 400000)
    print(f'Example2: {result}')
