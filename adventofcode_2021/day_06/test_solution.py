from functools import reduce

import pytest

from .solution import parse, solve, step

EXAMPLES = (
    ('3,4,3,1,2', 1, 5),
    ('3,4,3,1,2', 2, 6),
    ('3,4,3,1,2', 80, 5934),
    ('3,4,3,1,2', 256, 26984457539),
)

EXAMPLES_SIMULATE = (
    ('3,4,3,1,2', 0, {1: 1, 2: 1, 3: 2, 4: 1}),
    ('3,4,3,1,2', 1, {0: 1, 1: 1, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}),
    ('3,4,3,1,2', 2, {0: 1, 1: 2, 2: 1, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 1}),
)


@pytest.mark.parametrize('data,steps,expected', EXAMPLES)
def test_solve(data, steps, expected):
    assert solve(data, steps) == expected


@pytest.mark.parametrize('data,steps,expected', EXAMPLES_SIMULATE)
def test_simulate(data, steps, expected):
    data = parse(data)
    assert reduce(step, range(steps), data) == expected
