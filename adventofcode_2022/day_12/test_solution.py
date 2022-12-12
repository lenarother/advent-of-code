from .solution import solve, solve2

DATA = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def test_solve():
    assert solve(DATA) == 31


def test_solve2():
    assert solve2(DATA) == 29
