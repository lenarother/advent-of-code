import pytest

from .solution import Maze

EXAMPLES_POSITION = (
    (15, (0, 0), True),
    (10, (1, 1), True),
    (10, (4, 4), True),
    (10, (8, 2), True),
    (10, (2, 1), False),
    (10, (9, 6), False),
    (3, (0, 0), True),
    (3, (-1, 0), False),
    (3, (0, -1), False),
    (0, (0, 0), True),
)

EXAMPLES_POSSIBLE_MOVES = (
    (10, (1, 1), {(0, 1), (1, 2)}),
    (10, (5, 3), set()),
)

EXAMPLES_PATH = (
    (10, (1, 1), (7, 4), 11),
)

EXAMPLES_LOCATIONS = (
    (10, (1, 1), 0, 1),
    (10, (1, 1), 1, 3),
    (10, (1, 1), 2, 5),
    (10, (6, 5), 0, 1),
    (10, (6, 5), 1, 5),
    (10, (1, 1), 4, 9),
    (10, (1, 1), 5, 11),
)


@pytest.mark.parametrize('base,position,valid', EXAMPLES_POSITION)
def test_validate_position(base, position, valid):
    m = Maze(base)
    assert m.validate_position(*position) is valid


@pytest.mark.parametrize('base,position,moves', EXAMPLES_POSSIBLE_MOVES)
def test_get_possible_moves(base, position, moves):
    m = Maze(base)
    assert m.find_moves(position) == moves


@pytest.mark.parametrize('base,start,exit,expected', EXAMPLES_PATH)
def test_find_path_length(base, start, exit, expected):
    m = Maze(base)
    assert m.find_path_length(start, exit) == expected


@pytest.mark.parametrize('base,start,moves_count,expected', EXAMPLES_LOCATIONS)
def test_count_visited_locations(base, start, moves_count, expected):
    m = Maze(base)
    assert m.count_locations(start, moves_count) == expected
