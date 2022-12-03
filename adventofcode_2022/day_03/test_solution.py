import pytest

from .solution import (
    get_badge_type,
    get_item_type,
    get_priority,
    solve,
    solve2,
)

DATA = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


@pytest.mark.parametrize(
    'data, expected',
    (
        ('vJrwpWtwJgWrhcsFMMfFFhFp', 'p'),
        ('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'L'),
        ('PmmdzqPrVvPwwTWBwg', 'P'),
    )
)
def test_get_item_type(data, expected):
    assert get_item_type(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ('a', 1),
        ('z', 26),
        ('A', 27),
        ('Z', 52),
    )
)
def test_get_priority(data, expected):
    assert get_priority(data) == expected


@pytest.mark.parametrize(
    'a, b, c, expected',
    (
        ('vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'r'),  # noqa
        ('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw', 'Z'),  # noqa
    )
)
def test_get_badge_type(a, b, c, expected):
    assert get_badge_type(a, b, c) == expected


def test_solve():
    assert solve(DATA) == 157


def test_solve2():
    assert solve2(DATA) == 70
