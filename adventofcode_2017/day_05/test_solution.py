from .solution import get_new_offset_increase_2, solve

DATEN = """
0
3
0
1
-3
"""


def test_solve():
    assert solve(DATEN) == 5


def test_solve2():
    assert solve(DATEN, get_new_offset_increase_2) == 10
