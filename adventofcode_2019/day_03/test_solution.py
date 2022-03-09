import pytest

from .solution import solve, solve2

EXAMPLE_1 = """
R8,U5,L5,D3
U7,R6,D4,L4
"""

EXAMPLE_2 = """
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
"""

EXAMPLE_3 = """
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
"""

EXAMPLES = (
    (EXAMPLE_1, 6),
    (EXAMPLE_2, 159),
    (EXAMPLE_3, 135),
)

EXAMPLES_2 = (
    (EXAMPLE_1, 30),
    (EXAMPLE_2, 610),
    (EXAMPLE_3, 410),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected