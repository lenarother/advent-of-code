"""

https://adventofcode.com/2023/day/4

"""
import re
from dataclasses import dataclass


def parse_card(card_string):
    id = int(card_string.split(':')[0].replace('Card', '').strip())
    left_part, right_part = card_string.split('|')
    left_numbers = [int(i) for i in re.findall(r'(\d+) ', left_part)]
    right_numbers = [int(i) for i in re.findall(r'(\d+)', right_part)]
    return Card(id=id, left_numbers=left_numbers, right_numbers=right_numbers)


@dataclass
class Card:
    id: int
    left_numbers: list[int]  # wining numbers
    right_numbers: list[int]  # my numbers
    copies: int = 1

    def __str__(self):
        return str(self.id)

    def get_points(self):
        n = self.get_n_winning_cards()
        return 2 ** (n - 1) if n else 0

    def get_n_winning_cards(self):
        return len(set(self.left_numbers).intersection(self.right_numbers))


def solve(data):
    return sum([
        parse_card(l).get_points()
        for l in data.strip().split('\n')
    ])


def solve_2(data):
    cards = {}
    for l in data.strip().split('\n'):
        card = parse_card(l)
        cards[card.id] = card

    for card in cards.values():
        n = card.get_n_winning_cards()
        for i in range(1, n + 1):
            cards[card.id + i].copies += card.copies

    return sum([card.copies for card in cards.values()])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result_2 = solve_2(input_data)
    print(f'Example2: {result_2}')
