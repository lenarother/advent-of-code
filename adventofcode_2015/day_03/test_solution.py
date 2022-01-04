import pytest

from .solution import solve, solve2

EXAMPLES = (
    ('>', 2),
    ('^>v<', 4),
    ('^v^v^v^v^v', 2),
)

EXAMPLES_2 = (
    ('^v', 3),
    ('^>v<', 3),
    ('^v^v^v^v^v', 11),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected
