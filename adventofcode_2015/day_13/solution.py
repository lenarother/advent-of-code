"""Day 13: Knights of the Dinner Table

https://adventofcode.com/2015/day/13

"""
import re
from itertools import permutations

PAIR = re.compile(
    r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).'
)


def parse_matrix(data):
    return {
        (p1, p2): (1 if sign == 'gain' else -1) * int(happiness)
        for p1, sign, happiness, p2 in PAIR.findall(data)
    }


def parse_guests(data):
    guests = set()
    for p1, _, _, p2 in PAIR.findall(data):
        guests.add(p1)
        guests.add(p2)
    return list(guests)


def calc_happiness(arrangement, matrix):
    happiness = 0
    for p1, p2 in zip(arrangement[:-1], arrangement[1:]):
        happiness += matrix[(p1, p2)]
        happiness += matrix[(p2, p1)]
    p_first = arrangement[0]
    p_last = arrangement[-1]
    happiness += matrix[(p_first, p_last)]
    happiness += matrix[(p_last, p_first)]
    return happiness


def happiness_gen(guests, matrix):
    for arrangement in permutations(guests):
        yield calc_happiness(arrangement, matrix)


def solve(data):
    guests = parse_guests(data)
    matrix = parse_matrix(data)
    return max(happiness_gen(guests, matrix))


def add_yourself_to_guests(guests, matrix, me='Magda'):
    assert me not in guests
    for g in guests:
        matrix[(me, g)] = 0
        matrix[(g, me)] = 0
    guests.append(me)
    return guests, matrix


def solve2(data):
    guests = parse_guests(data)
    matrix = parse_matrix(data)
    guests, matrix = add_yourself_to_guests(guests, matrix)
    return max(happiness_gen(guests, matrix))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
