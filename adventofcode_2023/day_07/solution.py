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


@dataclasses.dataclass
class Hand:
    cards: str
    bid: int
    card_strength: str = CARD_STRENGTH
    use_joker: bool = False

    def _cards_lt(self, other):
        for self_card, other_card in zip(self.cards, other.cards):
            self_card_index = self.card_strength.index(self_card)
            other_card_index = self.card_strength.index(other_card)
            if not other_card_index == self_card_index:
                # Lower index is better
                return self_card_index > other_card_index
        return False

    def __lt__(self, other):
        if self.rank == other.rank:
            return self._cards_lt(other)
        return self.rank > other.rank

    @property
    def rank(self):
        # the lower rank the better hand
        hand = self.joker_cards if self.use_joker else self.cards
        return HAND_STRENGTH.index(get_hand_type(hand))

    @property
    def most_common_card(self):
        if self.cards.count('J') == 5:
            return "A"
        return Counter(
            self.cards.replace('J', '')
        ).most_common()[0][0]

    @property
    def joker_cards(self):
        return self.cards.replace('J', self.most_common_card)


def solve(data, card_strength=CARD_STRENGTH, use_joker=False):
    hands = [
        Hand(*i.split(" "), card_strength=card_strength, use_joker=use_joker)
        for i in data.strip().split("\n")
    ]
    hands.sort()
    return sum([
        (i + 1) * int(hand.bid)
        for i, hand in enumerate(hands)
    ])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, card_strength=CARD_STRENGTH_2, use_joker=True)
    print(f'Example2: {result}')
