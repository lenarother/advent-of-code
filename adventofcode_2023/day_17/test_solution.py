import pytest

from .solution import solve, solve_2

DATA = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

DATA_2 = """
111111111111
999999999991
999999999991
999999999991
999999999991
"""

EXAMPLES = (
    (DATA, 102),
)

EXAMPLES_2 = (
    (DATA, 94),
    (DATA_2, 71),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve_2(data, expected):
    assert solve_2(data) == expected
