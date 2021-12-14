import pytest

from .solution import Cave, solve

DATA = """
2199943210
3987894921
9856789892
8767896789
9899965678"""

DATA_SMALL = """
919
999"""

DATA_SMALL_BASIN = """
219
398
988"""

EXAMPLES = (
    (DATA, 15),
    (DATA_SMALL, 2),
)

EXAMPLES_POINTS = (
    (DATA_SMALL, (0, 0), False),
    (DATA_SMALL, (1, 0), True),
)

EXAMPLES_BASINS = (
    (DATA_SMALL_BASIN, 3),
    (DATA, 1134),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,point,expected', EXAMPLES_POINTS)
def test_is_lowest(data, point, expected):
    c = Cave(data)
    assert c.is_point_lowest(point) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_BASINS)
def test_find_basins(data, expected):
    c = Cave(data)
    assert c.find_basins() == expected
