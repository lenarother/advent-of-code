import pytest

from .solution import solve

EXAMPLES = (
    ("0 1 10 99 999", 1, 7),
    ("125 17", 1, 3),
    ("125 17", 2, 4),
    ("125 17", 6, 22),
    ("125 17", 6, 22),
    ("125 17", 25, 55312),
)


@pytest.mark.parametrize('data, iterations, expected', EXAMPLES)
def test_solve(data, iterations, expected):
    assert solve(data, iterations) == expected
