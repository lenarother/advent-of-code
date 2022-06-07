import pytest

from .solution import STATE_CHANGE_MAP_2, solve, turn

DATA = """
..#
#..
...
"""


@pytest.mark.parametrize(
    'data, n, expected',
    (
        (DATA, 7, 5),
        (DATA, 70, 41),
        (DATA, 10_000, 5587),
    )
)
def test_solve(data, n, expected):
    assert solve(data, n) == expected


@pytest.mark.parametrize(
    'data, n, expected',
    (
        (DATA, 100, 26),
    )
)
def test_solve2(data, n, expected):
    result = solve(data, n, states_map=STATE_CHANGE_MAP_2)
    assert result == expected


@pytest.mark.parametrize(
    'direction, state, new_direction',
    (
        # turn right
        ('U', '#', 'R'),
        ('R', '#', 'D'),
        ('D', '#', 'L'),
        ('L', '#', 'U'),

        # turn left
        ('U', '.', 'L'),
        ('R', '.', 'U'),
        ('D', '.', 'R'),
        ('L', '.', 'D'),

        # no turn
        ('U', 'W', 'U'),
        ('R', 'W', 'R'),
        ('D', 'W', 'D'),
        ('L', 'W', 'L'),

        # reverse
        ('U', 'F', 'D'),
        ('R', 'F', 'L'),
        ('D', 'F', 'U'),
        ('L', 'F', 'R'),
    )
)
def test_turn(direction, state, new_direction):
    assert turn(direction, state) == new_direction
