import pytest

from .solution import solve, solve2

DATA = """
Player 1 starting position: 4
Player 2 starting position: 8
"""

EXAMPLES = (
    (DATA, 739785),
)

EXAMPLES_2 = (
    (DATA, 444_356_092_776_315),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected
