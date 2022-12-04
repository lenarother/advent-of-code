import pytest

from .solution import has_full_overlap, has_overlap, pairs, solve

DATA = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


@pytest.mark.parametrize(
    'data, expected',
    (
        ('2-4,6-8', False),
        ('2-3,4-5', False),
        ('5-7,7-9', False),
        ('2-8,3-7', True),
        ('6-6,4-6', True),
        ('2-6,4-8', False),
    )
)
def test_has_full_overlap(data, expected):
    r1, r2 = next(pairs(data))
    assert has_full_overlap(r1, r2) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ('2-4,6-8', False),
        ('2-3,4-5', False),
        ('5-7,7-9', True),
        ('2-8,3-7', True),
        ('6-6,4-6', True),
        ('2-6,4-8', True),
    )
)
def test_has_overlap(data, expected):
    r1, r2 = next(pairs(data))
    assert has_overlap(r1, r2) == expected


def test_solve():
    assert solve(DATA) == 2
    assert solve(DATA, has_overlap) == 4
