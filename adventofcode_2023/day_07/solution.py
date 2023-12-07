"""Day 7: Camel Cards

https://adventofcode.com/2023/day/7

"""
import dataclasses
from collections import Counter

CARD_STRENGTH = "AKQJT98765432"
CARD_STRENGTH_2 = "AKQT98765432J"

HAND_STRENGTH = [
    "Five of a kind",
    "Four of a kind",
    "Full house",
    "Three of a kind",
    "Two pair",
    "One pair",
    "High card",
]


def get_hand_type(hand):
    cards = Counter(hand)
    if len(cards) == 1:
        return "Five of a kind"
    if len(cards) == 2 and cards.most_common()[0][1] == 4:
        return "Four of a kind"
    elif len(cards) == 2 and cards.most_common()[0][1] == 3:
        return "Full house"
    elif len(cards) == 3 and cards.most_common()[0][1] == 3:
        return "Three of a kind"
    elif len(cards) == 3 and cards.most_common()[0][1] == 2:
        return "Two pair"
    elif len(cards) == 4:
        return "One pair"
    elif len(cards) == 5:
        return "High card"


def cmp_hand_rank(first, second):
    """
    Returns:
    -1 -> the first is less than the second
     1 -> the first is greater than the second
     0 -> equal
    """
    first_rank = HAND_STRENGTH.index(get_hand_type(first))
    second_rank = HAND_STRENGTH.index(get_hand_type(second))
    if first_rank == second_rank:
        return 0
    elif first_rank < second_rank:
        return 1
    return -1


def cmp_card_rank(first, second, card_strength=CARD_STRENGTH):
    """
    Returns:
    -1 -> the first is less than the second
     1 -> the first is greater than the second
     0 -> equal
    """
    for f, s in zip(first, second):
        f_rank = card_strength.index(f)
        s_rank = card_strength.index(s)
        if f_rank < s_rank:
            return 1
        elif f_rank > s_rank:
            return -1
    return 0


@dataclasses.dataclass
class Hand:
    cards: str
    bid: int

    def __lt__(self, other):
        hand_result = cmp_hand_rank(self.cards, other.cards)
        if hand_result == 0:
            return cmp_card_rank(self.cards, other.cards) == -1
        return hand_result == -1


@dataclasses.dataclass
class Hand2:
    cards: str
    bid: int

    def __lt__(self, other):
        hand_result = cmp_hand_rank(self.prepared_hand, other.prepared_hand)
        if hand_result == 0:
            return cmp_card_rank(
                self.cards, other.cards, CARD_STRENGTH_2
            ) == -1
        return hand_result == -1

    @property
    def prepared_hand(self):
        if self.cards.count('J') == 5:
            return "AAAAA"
        mycards = self.cards.replace('J', '')
        cards = Counter(mycards)
        most_common = cards.most_common()[0][0]
        new_cards = self.cards.replace('J', most_common)
        return new_cards


def solve(data):
    hands = [Hand(*i.split(" ")) for i in data.strip().split("\n")]
    hands.sort()
    return sum([(i + 1) * int(hand.bid) for i, hand in enumerate(hands)])


def solve_2(data):
    hands = [Hand2(*i.split(" ")) for i in data.strip().split("\n")]
    hands.sort()
    return sum([(i + 1) * int(hand.bid) for i, hand in enumerate(hands)])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example2: {result}')
