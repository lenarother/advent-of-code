import pytest

from .solution import solve

DATA = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


@pytest.mark.parametrize(
    'data, n, expected',
    (
        (DATA, 1, 24000),
        (DATA, 3, 45000),
    )
)
def test_solve(data, n, expected):
    assert solve(data, n) == expected
