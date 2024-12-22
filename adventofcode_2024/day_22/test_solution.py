import pytest

from .solution import (
    calculate_n_next_number,
    calculate_next_number,
    solve,
    solve2,
)

DATA = """
1
10
100
2024
"""

DATA_2 = """
1
2
3
2024
"""

EXAMPLES = (
    ('123', 1, 15887950),
    (DATA, 2000, 37327623),
)


@pytest.mark.parametrize('data, n, expected', EXAMPLES)
def test_solve(data, n,  expected):
    assert solve(data, n) == expected


@pytest.mark.parametrize(
    'number, expected',
    (
            (123, 15887950),
            (15887950, 16495136),
    ),
)
def test_calculate_next_number(number, expected):
    assert calculate_next_number(number) == expected


@pytest.mark.parametrize(
    'number, n, expected',
    (
            (123, 1, 15887950),
            (15887950, 1, 16495136),
            (1, 2000, 8685429),
            (10, 2000, 4700978),
            (100, 2000, 15273692),
            (2024, 2000, 8667524),
    ),
)
def test_calculate_n_next_number(number, n, expected):
    assert calculate_n_next_number(number, n) == expected


@pytest.mark.parametrize(
    'data, n, expected',
    (
        ('123', 10, 6),
        (DATA_2, 2000, 23),
    ),
)
def test_solve2(data, n, expected):
    assert solve2(data, n) == expected
