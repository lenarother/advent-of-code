import pytest

from .solution import (
    calculate_distance,
    remove_collisions,
    solve,
    solve2,
    update_particles,
)

DATA = """
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
"""

DATA_2 = """
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
"""


def test_solve():
    assert solve(DATA) == 0


def test_solve2():
    assert solve2(DATA_2) == 1


@pytest.mark.parametrize(
    'data, expected',
    (
        (
            {0: {'p': [3, 0, 0], 'v': [2, 0, 0], 'a': [-1, 0, 0]}},
            {0: {'p': [4, 0, 0], 'v': [1, 0, 0], 'a': [-1, 0, 0]}},
        ),
        (
            {0: {'p': [4, 0, 0], 'v': [1, 0, 0], 'a': [-1, 0, 0]}},
            {0: {'p': [4, 0, 0], 'v': [0, 0, 0], 'a': [-1, 0, 0]}},
        ),
    ),
)
def test_update_particles(data, expected):
    assert update_particles(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ({0: {'p': [3, 0, 0], 'v': [2, 0, 0], 'a': [-1, 0, 0]}}, {0: 3}),
        ({0: {'p': [4, 0, 0], 'v': [1, 0, 0], 'a': [-1, 0, 0]}}, {0: 4}),
    ),
)
def test_calculate_distance(data, expected):
    assert calculate_distance(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        (
            {
                0: {'p': [0, 0, 0], 'v': [2, 0, 0], 'a': [-1, 0, 0]},
                1: {'p': [0, 0, 0], 'v': [1, 0, 0], 'a': [-1, 0, 0]},
                2: {'p': [1, 0, 0], 'v': [1, 0, 0], 'a': [-1, 0, 0]},
            },
            {
                2: {'p': [1, 0, 0], 'v': [1, 0, 0], 'a': [-1, 0, 0]},
            }
        ),
    ),
)
def test_remove_collisions(data, expected):
    assert remove_collisions(data) == expected
