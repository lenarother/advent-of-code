import pytest

from .solution import Grid, access_data, parse_discs, solve

EXAMPLES = (
    ("""
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     94T   0T    21T   77%
/dev/grid/node-x0-y1     87T   0T    23T   73%""", 0),
    ("""
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     94T   23T   21T   77%
/dev/grid/node-x0-y1     87T   0T    23T   73%""", 1),
    ("""
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     94T   23T   21T   77%
/dev/grid/node-x0-y1     87T   21T    23T   73%""", 2),
    ("""
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     94T   23T   21T   77%
/dev/grid/node-x0-y1     94T   23T   21T   77%
/dev/grid/node-x0-y2     87T   21T   23T   73%""", 4),
)

EXAMPLE_PARSE = (
    ("""
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     94T   0T    21T   77%""",
        {
            (0, 0): {'Used': 0, 'Avail': 21}
        }
     ),
    ("""
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     94T   0T    21T   77%
/dev/grid/node-x0-y1     94T   0T    21T   77%""",
        {
            (0, 0): {'Used': 0, 'Avail': 21},
            (0, 1): {'Used': 0, 'Avail': 21},
        }
     ),
)

GRID = """
Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%
"""

GRID_NULL_POSITION = (
    (GRID, (1, 1)),
)

GRID_NULL = (
    (GRID, 4),
)

GRID_WIDTH = (
    (GRID, 3),
)

GRID_STR = (
    (GRID, '..G._.#..'),
)

GRID_POSSIBLE_MOVES = (
    ('..G._.#..', 3, [1, 3, 5, 7]),
    ('_.G...#..', 3, [1, 3]),
    ('..G_..#..', 3, [0, 4]),
    ('._G...#..', 3, [0, 2, 4]),
)

GRID_APPLY_MOVE = (
    (GRID, 1, '._G...#..'),
)

GRID_ACCESS_DATA = (
    (GRID, 7),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLE_PARSE)
def test_parse(data, expected):
    assert parse_discs(data) == expected


@pytest.mark.parametrize('data,expected', GRID_NULL_POSITION)
def test_get_null_position(data, expected):
    assert Grid.get_null_coord(data) == expected


@pytest.mark.parametrize('data,expected', GRID_NULL)
def test_grid_null(data, expected):
    g = Grid(data)
    assert g.null == expected


@pytest.mark.parametrize('data,expected', GRID_WIDTH)
def test_get_width(data, expected):
    assert Grid.get_width(data) == expected


@pytest.mark.parametrize('data,expected', GRID_STR)
def test_grid_repr(data, expected):
    g = Grid(data)
    assert f'{g}' == expected


@pytest.mark.parametrize('data,width,expected', GRID_POSSIBLE_MOVES)
def test_grid_possible_moves(data, width, expected):
    g = Grid()
    g.str_data = data
    g.null = list(data).index('_')
    g.width = width
    assert list(g.get_possible_moves()) == expected


@pytest.mark.parametrize('data,move,expected', GRID_APPLY_MOVE)
def test_apply_move(data, move, expected):
    g = Grid(data)
    g.apply_move(move)
    assert str(g) == expected


@pytest.mark.parametrize('data,expected', GRID_ACCESS_DATA)
def test_access_data(data, expected):
    assert access_data(data) == expected
