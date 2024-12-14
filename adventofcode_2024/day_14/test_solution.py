import pytest

from .solution import solve

DATA = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


EXAMPLES = (
    (DATA, 100, 12),
)


@pytest.mark.parametrize('data, n, expected', EXAMPLES)
def test_solve(data, n, expected):
    assert solve(data, n) == expected
