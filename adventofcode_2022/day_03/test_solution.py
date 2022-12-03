import pytest

from .solution import (
    compartments,
    get_common_element,
    get_priority,
    groups,
    solve,
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
        (('vJrwpWtwJgWr', 'hcsFMMfFFhFp'), 'p'),
        (('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'), 'L'),
        (('PmmdzqPrV', 'vPwwTWBwg'), 'P'),
        (('vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'), 'r'),  # noqa
        (('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw'), 'Z'),  # noqa
    )
)
def test_get_common_element(data, expected):
    assert get_common_element(*data) == expected


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
    'data, data_iterator, expected',
    (
        (DATA, compartments, 157),
        (DATA, groups, 70),
    )
)
def test_solve(data, data_iterator, expected):
    assert solve(DATA, data_iterator) == expected
