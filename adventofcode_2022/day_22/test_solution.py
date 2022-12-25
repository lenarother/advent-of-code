import pytest

from .solution import get_direction, get_result, parse, parse_moves, solve, solve2

DATA = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""


def test_solve():
    assert solve(DATA) == 6032


def test_solve2():
    assert solve2(DATA) == 5031


@pytest.mark.parametrize(
    'current_direction, orientation, expected',
    (
        ((1, 0), 'R', (0, 1)),
        ((0, 1), 'L', (1, 0)),
        ((0, 1), 'R', (-1, 0)),
        ((-1, 0), 'R', (0, -1)),
        ((0, -1), 'R', (1, 0)),
        ((0, 1), 'L', (1, 0)),
        ((0, -1), 'L', (-1, 0)),
        ((-1, 0), 'L', (0, 1)),
        ((0, 1), 'L', (1, 0)),
    )
)
def test_get_direction(current_direction, orientation, expected):
    assert get_direction(current_direction, orientation) == expected


@pytest.mark.parametrize(
    'position, direction, expected',
    (
        ((1, 1), (1, 0), 1004),  # >
        ((1, 1), (0, 1), 1005),  # v
        ((1, 1), (-1, 0), 1006),  # <
        ((1, 1), (0, -1), 1007),  # ^
        ((8, 6), (1, 0), 6032)
    ),
)
def test_get_result(position, direction, expected):
    assert get_result(position, direction) == expected


def test_parse():
    area_map, moves = parse(DATA)
    assert len(area_map) == 48 + 16 + 32
    assert len(moves) == 13


@pytest.mark.parametrize(
    'data, expected',
    (
        (
            '10R5L5R10L4R5L5',
            [10, 'R', 5, 'L', 5, 'R', 10, 'L', 4, 'R', 5, 'L', 5]
        ),
    ),
)
def test_parse_moves(data, expected):
    assert parse_moves(data) == expected
