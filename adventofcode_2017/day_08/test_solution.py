from .solution import solve

DATA = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""


def test_solve():
    assert solve(DATA) == (1, 10)
