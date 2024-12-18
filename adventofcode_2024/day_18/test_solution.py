import pytest

from .solution import solve, solve2

DATA = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

EXAMPLES = (
    (DATA, 12, (6, 6), 22),
)

EXAMPLES_2 = (
    (DATA, 12, (6, 6), (6, 1)),
)


@pytest.mark.parametrize('data, n_bytes, max_p, expected', EXAMPLES)
def test_solve(data, n_bytes, max_p, expected):
    assert solve(data, n_bytes, max_p) == expected


@pytest.mark.parametrize('data, n_bytes, max_p, expected', EXAMPLES_2)
def test_solve_2(data, n_bytes, max_p, expected):
    assert solve2(data, n_bytes, max_p) == expected
