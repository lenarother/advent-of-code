import pytest

from .solution import solve, solve2

DATA = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

DATA_2 = """
Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4
"""

DATA_3 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

EXAMPLES = (
    (DATA, "4,6,3,5,6,3,5,2,1,0"),
    (DATA_2, "0,1,2"),
)

EXAMPLES_2 = (
    (DATA_3, 117440),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve_2(data, expected):
    assert solve2(data) == expected
