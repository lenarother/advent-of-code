import pytest

from .solution import solve, parse, count_fuel, count_step, solve3

EXAMPLES = (
    ('16,1,2,0,4,2,7,1,2,14', 37),
)

EXAMPLES2 = (
    ('16,1,2,0,4,2,7,1,2,14', 168),
)

EXAMPLES_COUNT_FUEL = (
    ('16,1,2,0,4,2,7,1,2,14', 1, 41),
    ('16,1,2,0,4,2,7,1,2,14', 2, 37),
    ('16,1,2,0,4,2,7,1,2,14', 3, 39),
    ('16,1,2,0,4,2,7,1,2,14', 10, 71),
)

EXAMPLES_COUNT_STEP = (
    (16, 5, 66),
    (1, 5, 10),
    (2, 5, 6),
)

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,position,expected', EXAMPLES_COUNT_FUEL)
def test_count_fuel(data, position, expected):
    data = parse(data)
    assert count_fuel(data, position,) == expected


@pytest.mark.parametrize('current_position,target,expected', EXAMPLES_COUNT_STEP)
def test_count_step(current_position, target, expected):
    assert count_step(current_position, target) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES2)
def test_solve2(data, expected):
    assert solve3(data) == expected
