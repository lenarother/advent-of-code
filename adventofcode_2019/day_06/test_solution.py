import pytest

from .solution import parse_data, solve, solve2

EXAMPLE = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

EXAMPLE2 = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""


@pytest.mark.parametrize(
    'data, expected',
    (
        ('COM)B', 1),
        ('COM)B\nB)C', 3),
        (EXAMPLE, 42),
    )
)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        (EXAMPLE2, 4),
    )
)
def test_solve2(data, expected):
    assert solve2(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ('COM)B', {'COM': {'B'}}),
        ('COM)B\nB)C', {'COM': {'B'}, 'B': {'C'}}),
    )
)
def test_parse_data(data, expected):
    assert parse_data(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ('COM)B', {'B': {'COM'}, 'COM': {'B'}}),
        ('COM)B\nB)C', {'COM': {'B'}, 'B': {'COM', 'C'}, 'C': {'B'}}),
    )
)
def test_parse_data_reverse(data, expected):
    assert parse_data(data, reverse=True) == expected
