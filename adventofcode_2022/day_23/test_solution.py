import pytest

from .solution import proposed_directions, solve, solve2

DATA = """
..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............
"""

DATA_SMALL = """
.....
..##.
..#..
.....
..##.
.....
"""


@pytest.mark.parametrize(
    'data, expected',
    (
        (DATA_SMALL, 25),
        (DATA, 110),
    )
)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        (DATA_SMALL, 4),
        (DATA, 20),
    )
)
def test_solve2(data, expected):
    assert solve2(data) == expected


@pytest.mark.parametrize(
    'n, expected',
    (
        (1, 'NSWE'),
        (2, 'SWEN'),
        (3, 'WENS'),
        (4, 'ENSW'),
        (5, 'NSWE'),
    )
)
def test_proposed_directions(n, expected):
    d = proposed_directions()
    while n:
        proposed = next(d)
        n -= 1
    assert proposed == expected
