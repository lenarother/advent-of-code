import pytest

from .solution import caught_layers, is_caught, parse, solve, solve2

DATA = """
0: 3
1: 2
4: 4
6: 4
"""


@pytest.mark.parametrize(
    'scan_range, t, expected',
    (
        (3, 0, True),
        (3, 4, True),
        (3, 8, True),
        (3, 12, True),
        (3, 1, False),
        (3, 2, False),
        (3, 3, False),
        (3, 5, False),

        (2, 0, True),
        (2, 2, True),
        (2, 4, True),
        (2, 6, True),
        (2, 1, False),
        (2, 3, False),
        (2, 5, False),
        (2, 7, False),

        (4, 0, True),
        (4, 6, True),
        (4, 12, True),
        (4, 1, False),
        (4, 2, False),
        (4, 13, False),
    )
)
def test_is_caught(scan_range, t, expected):
    assert is_caught(scan_range, t) == expected


def test_caught_layers():
    firewall = parse(DATA)
    assert caught_layers(firewall) == [0, 6]


def test_solve():
    assert solve(DATA) == 24


def test_solve2():
    assert solve2(DATA) == 10
