"""

https://adventofcode.com/2023/day/3

"""
import string
import re
from collections import defaultdict

SIGNS = string.punctuation.replace('.', '')
NEIGHBOUR_POINTS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1),
]


def get_position(i: int, ln: int) -> tuple[int, int]:
    """
    i -> index
    ln -> line length
    """
    x = i % ln
    y = i // ln
    return x, y


def get_neighbour_positions(n: str, data: str, ln: int, x: int, y: int) -> set[int]:
    """
    n -> number as string
    data -> input string without line breaks
    x, y -> number coordinates
    ln -> line length
    """
    neighbour_positions = []
    number_positions = [(x + i, y) for i in range(0, len(n))]

    for i in range(0, len(n)):
        for xi, yi in NEIGHBOUR_POINTS:
            new_x = x + xi + i
            new_y = y + yi

            if (
                0 <= new_x < ln and
                0 <= new_y < len(data) // ln and
                (new_x, new_y) not in number_positions
            ):
                neighbour_positions.append((new_y * ln) + new_x)

    return set(neighbour_positions)


def solve(data: str) -> int:
    """
    data -> input string
    """
    # line length
    ln = len(data.split("\n")[0])

    # remove line breaks
    data = data.replace("\n", "")

    # sum of parts
    result = 0

    # iterate through all numbers in input
    for num_match in re.finditer(r'(\d+)', data):
        num = num_match.group()  # number as string
        ind = num_match.start()  # number's index in input string
        x, y = get_position(ind, ln)
        neighbors = get_neighbour_positions(num, data, ln, x, y)

        # Add number to result if it is adjacent to any sign
        if any([data[i] in SIGNS for i in neighbors]):
            result += int(num)

    return result


def solve_2(data: str) -> int:
    """
    data -> input string
    """
    # line length
    ln = len(data.split("\n")[0])

    # remove line breaks
    data = data.replace("\n", "")

    # Keep information about numbers adjacent to a star
    # {star_index: list of adjacent numbers}
    stars = defaultdict(list)

    # iterate through all numbers in input
    for num_match in re.finditer(r'(\d+)', data):
        num = num_match.group()  # number as string
        ind = num_match.start()  # number's index in input string
        x, y = get_position(ind, ln)
        neighbors = get_neighbour_positions(num, data, ln, x, y)

        # Add numer to stars dictionary if adjacent to a star
        for i in neighbors:
            if data[i] == "*":
                stars[i].append(num)

    # Find stars that are adjacent to two numbers and calculate final result
    return sum([
        int(v[0]) * int(v[1])
        for v in stars.values()
        if len(v) == 2
    ])


if __name__ == '__main__':

    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result_2 = solve_2(input_data)
    print(f'Example1: {result_2}')