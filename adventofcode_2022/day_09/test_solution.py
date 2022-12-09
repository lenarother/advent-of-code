import pytest

from .solution import find_direction, is_touching, solve, solve2

DATA = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

DATA2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


def test_solve():
    assert solve(DATA) == 13


def test_solve2():
    assert solve2(DATA) == 1
    assert solve2(DATA2) == 36


@pytest.mark.parametrize(
    'p1, p2, expected',
    (
        ((0, 0), (0, 0), True),
        ((0, 0), (0, 10), False),
        ((0, 0), (0, 1), True),
        ((0, 0), (0, -1), True),
        ((0, 0), (1, 1), True),
        ((0, 0), (-1, -1), True),
        ((0, 0), (1, -1), True),
        ((0, 0), (-1, 1), True),
        ((0, 0), (-1, 2), False),
        ((0, 0), (0, 2), False),
    )
)
def test_is_touching(p1, p2, expected):
    assert is_touching(p1, p2) == expected


@pytest.mark.parametrize(
    'h, t, expected',
    (
        ((4, -2), (3, 0), 'RU'),
        ((1, 1), (3, 2), 'LU'),
        ((3, 2), (1, 1), 'RD'),
        ((-3, -2), (-1, -1), 'LU'),
        ((1, 1), (3, 3), 'LU'),
    )
)
def test_find_direction(h, t, expected):
    assert find_direction(h, t) == expected
