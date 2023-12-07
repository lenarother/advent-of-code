from .solution import CARD_STRENGTH_2, solve

DATA = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


def test_solve():
    assert solve(DATA) == 6440
    assert solve(DATA, card_strength=CARD_STRENGTH_2, use_joker=True) == 5905
