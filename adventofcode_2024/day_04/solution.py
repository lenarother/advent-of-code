"""Day 4: Ceres Search

https://adventofcode.com/2024/day/4

"""
import numpy as np


def check_left_right(data):
    return data.count('XMAS') + data[::-1].count('XMAS')


def check_up_down(data):
    data_as_lists = []
    for i in data.strip().split('\n'):
        data_as_lists.append([j for j in i])
    data_rotates = '\n'.join(map(''.join, zip(*reversed(data_as_lists))))
    return check_left_right(data_rotates)


def check_diagonal(data):
    data_as_lists = []
    for i in data.strip().split('\n'):
        data_as_lists.append([j for j in i])
    # https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
    matrix = np.array(data_as_lists)
    diags = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0] + 1, matrix.shape[1])]
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1] - 1, -matrix.shape[0], -1))
    data_diagonal = '\n'.join([''.join(n.tolist()) for n in diags])
    return check_left_right(data_diagonal)


def solve(data):
    return check_left_right(data) + check_up_down(data) + check_diagonal(data)


def get_letters_dict(data):
    """Get dictionary where key is coordinate and value a letter."""
    letters = {}
    for y, row in enumerate(data.strip().split('\n')):
        for x, letter in enumerate(row):
            letters[(x, y)] = letter
    return letters


def check_letter(position, letters):
    """Check if a letter at given position is the middle of a MAS-MAS cross."""
    if letters[position] != 'A':
        return 0
    x, y = position
    x_letters = ''.join([
            letters.get((x - 1, y - 1), ''),
            letters.get((x + 1, y - 1), ''),
            letters.get((x - 1, y + 1), ''),
            letters.get((x + 1, y + 1), ''),
    ])
    if x_letters in ['MSMS', 'SSMM', 'MMSS', 'SMSM']:
        return 1
    return 0


def solve2(data):
    letters = get_letters_dict(data)
    return sum([check_letter(position, letters) for position in letters])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')