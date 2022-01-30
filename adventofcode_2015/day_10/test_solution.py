import pytest

from .solution import solve, step

EXAMPLES = (
    ('1', '11'),
    ('11', '21'),
    ('21', '1211'),
    ('1211', '111221'),
    ('111221', '312211'),
    ('111221', '312211'),
)

EXAMPLES_SOLVE = (
    ('1', 5, 6),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_step(data, expected):
    assert step(data) == expected


@pytest.mark.parametrize('data,steps,expected', EXAMPLES_SOLVE)
def test_solve(data, steps, expected):
    assert solve(data, steps) == expected
