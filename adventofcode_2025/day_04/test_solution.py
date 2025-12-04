import pytest

from .solution import solve, solve2

DATA = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

EXAMPLES = (
    (DATA, 13),
)
EXAMPLES2 = (
    (DATA, 43),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES2)
def test_solve2(data, expected):
    assert solve2(data) == expected
