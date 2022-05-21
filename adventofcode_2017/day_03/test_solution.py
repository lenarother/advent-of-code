import pytest

from .solution import solve, spiral, value


@pytest.mark.parametrize(
    'n, expected',
    (
        (1, (0, 0)),
        (2, (1, 0)),
        (3, (1, 1)),
        (12, (2, 1)),
        (23, (0, -2)),
    ),
)
def test_spiral_generator(n, expected):
    s = spiral()

    while n:
        position = next(s)
        n -= 1

    assert position == expected


@pytest.mark.parametrize(
    'square, steps',
    (
        (1, 0),
        (12, 3),
        (1024, 31),
    ),
)
def test_solve(square, steps):
    assert solve(square) == steps


@pytest.mark.parametrize(
    'steps, v',
    (
        (1, 1),
        (2, 1),
        (4, 4),
        (5, 5),
        (6, 10),
        (7, 11),
        (8, 23),
    ),
)
def test_value(steps, v):
    value_gen = value()

    while steps:
        val = next(value_gen)
        steps -= 1

    assert val == v
