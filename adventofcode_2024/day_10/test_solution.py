import pytest

from .solution import solve, solve2

DATA_1 = """
0123
1234
8765
9876
"""

DATA_2 = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

EXAMPLES = (
    (DATA_1, 1),
    (DATA_2, 36),
)

EXAMPLES_2 = (
    (DATA_2, 81),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve_2(data, expected):
    assert solve2(data) == expected
