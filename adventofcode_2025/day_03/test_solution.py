import pytest

from .solution import solve

DATA = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


@pytest.mark.parametrize(
    'data, n, expected',
    (
        (DATA, 2, 357),
        (DATA, 12, 3121910778619),
    )
)
def test_solve(data, n, expected):
    assert solve(data, n) == expected
