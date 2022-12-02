import pytest

from .solution import get_shape_score, score_round, score_round2, solve

DATA = """
A Y
B X
C Z
"""


@pytest.mark.parametrize(
    'data,expected',
    (
        ('ROCK', 1),
        ('PAPER', 2),
        ('SCISSORS', 3),
    ),
)
def test_get_shape_score(data, expected):
    assert get_shape_score(data) == expected


@pytest.mark.parametrize(
    'data,expected',
    (
        ('A Y', 8),  # Rock - Paper
        ('B X', 1),   # Paper - Rock
        ('C Z', 6),  # Scissors - Scissors
    ),
)
def test_score_round(data, expected):
    assert score_round(data) == expected


def test_solve():
    assert solve(DATA) == 15


def test_solve2():
    assert solve(DATA, score_round2) == 12
