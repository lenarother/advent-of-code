import pytest

from .solution import get_str_hash, solve, solve_2

DATA = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""


@pytest.mark.parametrize(
    'data,expected',
    (
        ('HASH', 52),
        ('rn', 0),
        ('rn=1', 30),
        ('cm-', 253),
        ('qp=3', 97),
        ('cm=2', 47),
        ('qp-', 14),
        ('pc=4', 180),
        ('ot=9', 9),
        ('ab=5', 197),
        ('pc-', 48),
        ('pc=6', 214),
        ('ot=7', 231),
    )
)
def test_get_str_value(data, expected):
    assert get_str_hash(data) == expected


def test_solve():
    assert solve(DATA) == 1320


def test_solve_2():
    assert solve_2(DATA) == 145
