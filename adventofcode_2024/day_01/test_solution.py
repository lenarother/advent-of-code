import pytest

from .solution import solve, solve2

DATA = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
EXAMPLES = (
    (DATA, 11),
)

EXAMPLES_2 = (
    (DATA, 31),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected
