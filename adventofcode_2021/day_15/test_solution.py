import pytest

from .solution import increase_row, solve, solve2

DATA = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

EXAMPLES = (
    (DATA, 40),
)


EXAMPLES_2 = (
    (DATA, 315),
)

EXAMPLES_INCREASE_ROW = (
    ('1163751742', 1, '2274862853'),
    ('1381373672', 1, '2492484783'),
    ('3694931569', 1, '4715142671'),
    ('1163751742', 0, '1163751742'),
    ('1163751742', 2, '3385973964'),

)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,n,expected', EXAMPLES_INCREASE_ROW)
def test_increase_row(data, n, expected):
    assert increase_row(data, n) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected
