import pytest

from .solution import Maze, find_all_paths, solve

MAZE = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########"""

EXAMPLES = (
    (MAZE, 14),
)

EXAMPLES_PATH = (
        (MAZE, (0, 1), 2),
        (MAZE, (0, 2), 8),
        (MAZE, (1, 2), 6),
)

EXSAMPLES_POSITION = (
        (MAZE, '0', (1, 1)),
        (MAZE, '1', (3, 1)),
        (MAZE, '2', (9, 1)),
        (MAZE, '3', (9, 3)),
        (MAZE, '4', (1, 3)),
)

EXSAMPLES_LOCATIONS = (
    (MAZE, set(['0', '1', '2', '3', '4'])),
)

EXSAMPLES_PATHS = (
    (MAZE, {
        frozenset({'0', '1'}): 2,
        frozenset({'0', '2'}): 8,
        frozenset({'0', '3'}): 10,
        frozenset({'0', '4'}): 2,
        frozenset({'1', '2'}): 6,
        frozenset({'1', '3'}): 8,
        frozenset({'1', '4'}): 4,
        frozenset({'2', '3'}): 2,
        frozenset({'2', '4'}): 10,
        frozenset({'3', '4'}): 8,
    }),
)

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('maze,ch,position', EXSAMPLES_POSITION)
def test_find_position(maze, ch, position):
    maze = Maze(maze)
    assert maze.find_position(ch) == position


@pytest.mark.parametrize('maze,expected', EXSAMPLES_LOCATIONS)
def test_find_locations(maze, expected):
    maze = Maze(maze)
    assert maze.find_locations() == expected


@pytest.mark.parametrize('maze,expected', EXSAMPLES_PATHS)
def test_find_all_paths(maze, expected):
    assert find_all_paths(maze) == expected
