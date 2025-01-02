import pytest

from .solution import solve

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


EXAMPLES = (
    (DATA, "4,6,3,5,6,3,5,2,1,0"),
    (DATA_2, "0,1,2"),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected
