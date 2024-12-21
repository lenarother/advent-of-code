import pytest

from .solution import solve, solve2

DATA = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
"""

DATA_2 = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

DATA_3 = """Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176"""

EXAMPLES = (
    (DATA, 280),
    (DATA_2, 480),
)
EXAMPLES_2 = (
    (DATA_3, 280),
)

#@pytest.mark.parametrize('data,expected', EXAMPLES)
#def test_solve(data, expected):
#    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve_2(data, expected):
    assert solve2(data) == expected