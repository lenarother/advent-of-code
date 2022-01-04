import pytest

from .solution import calc_present_area, calculate_ribbon_length, solve

EXAMPLES = (
    ('2x3x4', calc_present_area, 58),
    ('1x1x10', calc_present_area, 43),
    ('1x1x10\n2x3x4', calc_present_area, 101),
    ('2x3x4', calculate_ribbon_length, 34),
    ('1x1x10', calculate_ribbon_length, 14),
    ('1x1x10\n2x3x4', calculate_ribbon_length, 48),
)


@pytest.mark.parametrize('data,func,expected', EXAMPLES)
def test_solve(data, func, expected):
    assert solve(data, func) == expected
