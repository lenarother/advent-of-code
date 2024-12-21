import pytest

from .solution import solve, solve2

DATA = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

DATA_2 = """
r, wr, b, g, bwu, rb, gb, br

rrbgbr
"""

DATA_3 = """
r, wr, b, g, bwu, rb, gb, br

gbbr
"""

EXAMPLES = (
    (DATA, 6),
)

EXAMPLES_2 = (
    (DATA, 16),
    (DATA_2, 6),
    (DATA_3, 4),
)


#@pytest.mark.parametrize('data,expected', EXAMPLES)
#def test_solve(data, expected):
#    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve_2(data, expected):
    assert solve2(data) == expected
