import pytest

from .solution import solve

DATA = """
AAAA
BBCD
BBCC
EEEC
"""
DATA_2 = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

DATA_3 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

EXAMPLES = (
    (DATA, 140),
    #(DATA_2, 52),
    #(DATA_3, 1930),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected
