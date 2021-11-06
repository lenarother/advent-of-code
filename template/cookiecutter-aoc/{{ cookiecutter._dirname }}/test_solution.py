import pytest

from .solution import solve

EXAMPLES = (
    (1, 1),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected
