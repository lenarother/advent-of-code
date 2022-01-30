import pytest

from .solution import solve, solve2

DATA = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

EXAMPLES = (
    (DATA, 1000, 1120),
)

EXAMPLES_2 = (
    (DATA, 1000, 689),
)


@pytest.mark.parametrize('data,t,expected', EXAMPLES)
def test_solve(data, t, expected):
    assert solve(data, t) == expected


@pytest.mark.parametrize('data,t,expected', EXAMPLES_2)
def test_solve2(data, t, expected):
    assert solve2(data, t) == expected
