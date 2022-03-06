from .solution import solve, solve2

DATA = """
5 1 9 5
7 5 3
2 4 6 8
"""

DATA_2 = """
5 9 2 8
9 4 7 3
3 8 6 5
"""


def test_solve():
    assert solve(DATA) == 18


def test_solve2():
    assert solve2(DATA_2) == 9
