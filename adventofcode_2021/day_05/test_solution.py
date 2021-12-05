import pytest

from .solution import get_points, parse, solve

DATA = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

EXAMPLES = (
    (DATA, True, 12),
    (DATA, False, 5),
)

EXAMPLES_POINTS = (
    #
    # NO DIAGONAL
    #
    ('1,1 -> 1,3', 0, [(1, 1), (1, 2), (1, 3)]),
    ('9,7 -> 7,7', 0, [(9, 7), (8, 7), (7, 7), ]),
    ('1,1 -> 3,3', 0, []),
    ('9,7 -> 7,9', 0, []),
    #
    # DIAGONAL
    #
    ('1,1 -> 1,3', 1, [(1, 1), (1, 2), (1, 3)]),
    ('9,7 -> 7,7', 1, [(9, 7), (8, 7), (7, 7)]),
    ('1,1 -> 3,3', 1, [(1, 1), (2, 2), (3, 3)]),
    ('9,7 -> 7,9', 1, [(9, 7), (8, 8), (7, 9)]),
)


@pytest.mark.parametrize('data,diagonal,expected', EXAMPLES)
def test_solve(data, diagonal, expected):
    assert solve(data, diagonal) == expected


@pytest.mark.parametrize('data,diagonal,expected', EXAMPLES_POINTS)
def test_get_points(data, diagonal, expected):
    p1, p2 = parse(data)
    assert list(get_points(p1, p2, diagonal)) == expected
