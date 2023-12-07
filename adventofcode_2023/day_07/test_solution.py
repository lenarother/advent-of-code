from .solution import solve, solve_2

DATA = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_solve():
    assert solve(DATA) == 6440


def test_solve_2():
    assert solve_2(DATA) == 5905
