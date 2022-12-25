import pytest

from .solution import solve, solve2

DATA = """
30373
25512
65332
33549
35390
"""

def test_solve():
    assert solve(DATA) == 21


def test_solve2():
    assert solve2(DATA) == 8
