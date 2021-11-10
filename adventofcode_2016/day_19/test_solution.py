import pytest

from .solution import solve

EXAMPLES = (
    (1, 1),
    (2, 1),
    (3, 3),
    (4, 1),
    (5, 3),
    (6, 5),
    (7, 7),
)

EXAMPLES_ACROSS = (
    (1, 1),
    (2, 1),
    (3, 3),
    (4, 1),
    (5, 2),
    (6, 3),
    (7, 5),
    (8, 7),
    (9, 9),
    (10, 1),
    (11, 2),
    (12, 3),
    (13, 4),
    (1000, 271)
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_ACROSS)
def test_solve_across(data, expected):
    assert solve(data, across=True) == expected
