import pytest

from .solution import solve

EXAMPLES = (
    ("""Disc #1 has 5 positions; at time=0, it is at position 4.""", 0),
    ("""Disc #1 has 2 positions; at time=0, it is at position 0.""", 1),
    ("""Disc #1 has 17 positions; at time=0, it is at position 15.""", 1),
    ("""Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.""", 5),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected
