import pytest

from .solution import find_target, solve, solve2


@pytest.mark.parametrize(
    'data, expected',
    (
        ('ne,ne,ne', (3, 1.5)),
        ('ne,ne,sw,sw', (0, 0)),
        ('ne,ne,s,s', (2, -1)),
        ('se,sw,se,sw,sw', (-1, -2.5)),
    )
)
def test_find_target(data, expected):
    assert find_target(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ('ne,ne,ne', 3),
        ('ne,ne,sw,sw', 0),
        ('ne,ne,s,s', 2),
        ('se,sw,se,sw,sw', 3),
    )
)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ('ne,ne,ne', 3),
        ('ne,ne,sw,sw', 2),
    )
)
def test_solve2(data, expected):
    assert solve2(data) == expected
