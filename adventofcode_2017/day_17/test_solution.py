import pytest

from .solution import solve, solve2, spinlock


@pytest.mark.parametrize(
    'step, n, expected',
    (
        (3, 1, [0, 1]),
        (3, 2, [0, 2, 1]),
        (3, 3, [0, 2, 3, 1]),
        (3, 4, [0, 2, 4, 3, 1]),
    )
)
def test_spinlock(step, n, expected):
    s = spinlock(step)
    while n:
        result = next(s)
        n -= 1
    assert result == expected


def test_solve():
    assert solve(3) == 638


@pytest.mark.parametrize(
    'step, n, expected',
    (
        (3, 1, 1),
        (3, 2, 2),
        (3, 3, 2),
        (3, 4, 2),
        (3, 5, 5),
        (3, 6, 5),
        (3, 7, 5),
        (3, 8, 5),
        (3, 9, 9),
        (304, 1, 1),
        (304, 2, 1),
        (304, 3, 3),
        (304, 4, 3),
        (304, 5, 3),
        (304, 6, 6),
    )
)
def test_solve2(step, n, expected):
    assert solve2(step, n) == expected
