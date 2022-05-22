import pytest

from .solution import redistribute, solve


@pytest.mark.parametrize(
    'before, after',
    (
        ((0, 2, 7, 0), (2, 4, 1, 2)),
        ((2, 4, 1, 2), (3, 1, 2, 3)),
        ((3, 1, 2, 3), (0, 2, 3, 4)),
        ((0, 2, 3, 4), (1, 3, 4, 1)),
        ((1, 3, 4, 1), (2, 4, 1, 2)),
    )
)
def test_redistribute(before, after):
    assert redistribute(before) == after


def test_solve():
    assert solve('0 2   7   0') == 5
