import pytest

from .solution import get_longer_bridge, solve

DATA = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
"""


@pytest.mark.parametrize(
    'data,expected',
    (
        ('', 0),
        ('2/2\n2/3', 0),
        ('0/2\n2/2', 6),
        ('0/2\n2/2', 6),
        ('0/2\n2/3\n2/10', 14),
        ('0/2\n2/2\n2/10', 18),
        (DATA, 31),
    )
)
def test_get_strongest_bridge(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize(
    'data,expected',
    (
        ('', 0),
        ('2/2\n2/3', 0),
        ('0/2\n2/2', 6),
        ('0/2\n2/2', 6),
        ('0/2\n2/3\n2/10', 14),
        ('0/2\n2/2\n2/10', 18),
        (DATA, 19),
    )
)
def test_get_longest_bridge(data, expected):
    assert solve(data, get_longer_bridge) == expected
