import pytest

from .solution import solve, solve_all

DATA = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

EXAMPLES = (
    (DATA, 46),
)


def test_solve():
    assert solve(DATA, ((0, 0), 'R')) == 46


def test_solve_all():
    assert solve_all(DATA) == 51
