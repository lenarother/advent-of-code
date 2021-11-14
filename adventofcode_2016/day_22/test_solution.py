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

EXAMPLE_ACCESS_DATA = (
    ("""
Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%""", 7),
)

EXAMPLE_ACCESS_DATA = (
    ("""
Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%""",
     """
..G
._.
#.."""),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLE_PARSE)
def test_parse(data, expected):
    assert parse_discs(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLE_ACCESS_DATA)
def test_grid(data, expected):
    assert f'{Grid(data)}' == expected
