import pytest

from .solution import solve, solve2

EXAMPLES = (
    ("2333133121414131402", 1928),
)
EXAMPLES_2 = (
    ("2333133121414131402", 2858),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve_2(data, expected):
    assert solve2(data) == expected
