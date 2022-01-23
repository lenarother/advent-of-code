import pytest

from .solution import calculate_entire_fuel, calculate_fuel, solve

DATA = """
12
14
1969
100756
"""

EXAMPLES_FUEL = (
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
)

EXAMPLES_FUEL_2 = (
    (12, 2),
    (14, 2),
    (1969, 966),
    (100756, 50346),
)

EXAMPLES = (
    (DATA, 34241),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_FUEL)
def test_calculate_fuel(data, expected):
    assert calculate_fuel(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_FUEL_2)
def test_calculate_entire_fuel(data, expected):
    assert calculate_entire_fuel(data) == expected
