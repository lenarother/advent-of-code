"""Day 4: Secure Container

https://adventofcode.com/2019/day/4

"""
import re


def validate_is_increasing(num_str):
    return all([i <= j for i, j in zip(num_str[:-1], num_str[1:])])


def validate_has_repetition(num_str):
    return bool(re.search(r'(\d)\1+', num_str))


def validate_has_repetition_length_two(num_str):
    return any([
        i.span()[1] - i.span()[0] == 2
        for i in re.finditer(r'(\d)\1+', num_str)
    ])


def is_valid(num):
    num_str = f'{num}'
    return (
        validate_is_increasing(num_str) and
        validate_has_repetition(num_str)
    )


def is_valid_strict(num):
    num_str = f'{num}'
    return (
        validate_is_increasing(num_str) and
        validate_has_repetition_length_two(num_str)
    )


def solve(validation_function=is_valid):
    return sum([
        validation_function(i) for i in range(158126, 624574 + 1)
    ])


if __name__ == '__main__':
    result = solve()
    print(f'Example1: {result}')

    result = solve(validation_function=is_valid_strict)
    print(f'Example2: {result}')
