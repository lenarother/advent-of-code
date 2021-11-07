import pytest

from .solution import find_longest_path, get_moves, solve

EXAMPLES = (
    ('ihgpwlah', 'DDRRRD'),
    ('kglvqrro', 'DDUDRLRRUDRD'),
    ('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'),
)

EXAMPLES_MOVES = (
    ('hijkl', '', (0, 0), [('D', (0, 1))]),
    ('hijkl', 'D', (0, 1), [('DU', (0, 0)), ('DR', (1, 1))]),
    ('hijkl', 'DR', (1, 1), []),
    ('hijkl', 'DU', (0, 0), [('DUR', (1, 0))]),
    ('hijkl', 'DUR', (1, 0), []),
)

EXAMPLES_LONGEST_PATH = (
    ('ihgpwlah', 370),
    ('kglvqrro', 492),
    ('ulqzkmiv', 830),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('salt,path,position,expected', EXAMPLES_MOVES)
def test_get_moves(salt, path, position, expected):
    assert get_moves(salt, path, position) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_LONGEST_PATH)
def test_find_longest_path(data, expected):
    assert find_longest_path(data) == expected
