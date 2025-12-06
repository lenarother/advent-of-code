import pytest

from .solution import solve, solve2

DATA = """
1   0   1   0
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""

DATA_2 = """
0   0   0   0
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""


EXAMPLES = (
    (DATA, 4277556),
)
EXAMPLES_2 = (
    (DATA_2, 3263827),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve_2(data, expected):
    assert solve2(data) == expected
