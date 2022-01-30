import pytest

from .solution import solve, solve2

EXAMPLES = (
    ('turn on 499,499 through 500,500', 4),
    ('toggle 0,0 through 999,0', 1000),
    ("""
turn on 499,499 through 500,500
turn off 499,499 through 500,500""", 0),
)

EXAMPLES_2 = (
    ('turn on 0,0 through 0,0', 1),
    ('toggle 0,0 through 999,999', 2000000),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected
