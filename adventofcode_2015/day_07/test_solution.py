import pytest

from .solution import solve

DATA = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

EXAMPLES = (
    ('123 -> x', 'x', 123),
    ('456 -> y', 'y', 456),
    (DATA, 'x', 123),
    (DATA, 'd', 72),
    (DATA, 'e', 507),
    (DATA, 'f', 492),
    (DATA, 'g', 114),
    (DATA, 'h', 65412),
    (DATA, 'i', 65079),
    (DATA, 'y', 456),
)


@pytest.mark.parametrize('data,var,expected', EXAMPLES)
def test_solve(data, var, expected):
    assert solve(data, var) == expected
