import pytest

from .solution import solve, solve2

DATA = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

DATA2 = """
L50
"""

DATA3 = """
L50
L50
L50
"""

DATA4 = """
L50
L100
L100
"""

DATA5 = """
L50
R1
L1
"""


@pytest.mark.parametrize(
    'data,expected',
    (
        (DATA, 3),
    )
)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize(
    'data,expected',
    (
        (DATA, 6),
        (DATA2, 1),
        (DATA3, 2),
        (DATA4, 3),
        (DATA5, 2),
    )
)
def test_solve2(data, expected):
    assert solve2(data) == expected
