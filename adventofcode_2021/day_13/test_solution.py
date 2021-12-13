import pytest

from .solution import fold_dot, solve1, solve2

DATA = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

MESSAGE = """
#####
#...#
#...#
#...#
#####"""

EXAMPLES = (
    (DATA, 17),
)

EXAMPLES_FOLD_X = (
    ((0, 0), 5, (0, 0)),
    ((2, 1), 5, (2, 1)),
    ((6, 0), 5, (4, 0)),
    ((8, 0), 5, (2, 0)),
)

EXAMPLES_MESSAGE = (
    (DATA, MESSAGE),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve1(data, expected):
    assert solve1(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_MESSAGE)
def test_solve2(data, expected):
    assert solve2(data) == expected.strip()


@pytest.mark.parametrize('coord,val,expected', EXAMPLES_FOLD_X)
def test_fold_along_x(coord, val, expected):
    assert fold_dot(coord, ('x', val)) == expected
