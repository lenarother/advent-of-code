"""Day 22: Monkey Market

https://adventofcode.com/2024/day/22

"""
from collections import defaultdict


def input_gen(data):
    for i in data.strip().split('\n'):
        yield int(i)


def calculate_next_number(number):
    number = ((number * 64) ^ number) % 16777216
    number = ((int(number / 32) ^ number)) % 16777216
    number = ((number * 2048) ^ number) % 16777216
    return number


def calculate_n_next_number(number, n=1):
    while n:
        number = calculate_next_number(number)
        n -= 1
    return number


def get_price_from_number(number):
    return int(repr(number)[-1])


def next_prices_diffs(number, n=1):
    prices = []
    diffs = []
    initial_price = get_price_from_number(number)
    while n:
        number = calculate_next_number(number)
        price = get_price_from_number(number)
        prices.append(price)
        diffs.append(price - initial_price)
        initial_price = price
        n -= 1
    return prices, diffs


def update_dict(result_dict, prices, diffs):
    visited = set()
    for i in range(len(prices) - 3):
        change_sequence = (diffs[i], diffs[i + 1], diffs[i + 2], diffs[i + 3])
        price = prices[i + 3]
        if change_sequence not in visited:
            result_dict[change_sequence] += price
            visited.add(change_sequence)


def solve(data, n=1):
    return sum([calculate_n_next_number(i, n) for i in input_gen(data)])


def solve2(data, n=10):
    result_dict = defaultdict(int)
    for i in input_gen(data):
        prices, diffs = next_prices_diffs(i, n)
        update_dict(result_dict, prices, diffs)
    return max(result_dict.values())


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 2000)
    print(f'Example1: {result}')

    result = solve2(input_data, 2000)
    print(f'Example1: {result}')
