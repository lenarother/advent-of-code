import pytest

from .solution import solve, solve2

DATA = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""


@pytest.mark.parametrize(
    'data, expected',
    (
        ('0 <-> 2', 2),
        (DATA, 6),
    )
)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ('0 <-> 0', 1),
        ('0 <-> 0\n1 <-> 1\n2 <-> 2', 3),
        (DATA, 2),
    )
)
def test_solve2(data, expected):
    assert solve2(data) == expected
