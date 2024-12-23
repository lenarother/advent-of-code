import pytest

from .solution import solve, solve2

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
DATA_4 = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""
DATA_5 = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""

EXAMPLES = (
    (DATA, 140),
    (DATA_2, 772),
    (DATA_3, 1930),
)

EXAMPLES_2 = (
    (DATA, 80),
    #(DATA_3, 1206),
    #(DATA_4, 236),
    #(DATA_5, 368),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected

@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve_2(data, expected):
    assert solve2(data) == expected
