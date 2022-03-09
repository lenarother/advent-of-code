import pytest

from .solution import points, solve, solve2

DATA = """
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""

EXAMPLES = (
    (DATA, 4),
)

EXAMPLES_2 = (
    (DATA, 3),
)

EXAMPLES_POINTS = (
    ((5, 5), 2, 2, {(5, 5), (6, 5), (5, 6), (6, 6)}),
)


@pytest.mark.parametrize('start,x,y,expected', EXAMPLES_POINTS)
def test_points(start, x, y, expected):
    assert set(points(start, x, y)) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected
