import pytest

from .solution import solve, solve2

DATA = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

EXAMPLES = (
    (DATA, 3),
)
EXAMPLES2 = (
    (DATA, 14),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES2)
def test_solve2(data, expected):
    assert solve2(data) == expected
