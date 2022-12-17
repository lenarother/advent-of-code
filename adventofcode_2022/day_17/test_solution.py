import pytest

from .solution import solve

MOVES = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'


@pytest.mark.parametrize(
    'n, expected',
    (
        # (1, 1),
        # (2, 4),
        # (3, 6),
        # (4, 7),
        # (5, 9),
        # (6, 10),
        # (7, 13),
        # (8, 15),
        # (9, 17),
        # (10, 17),
        # (2022, 3068),
        (80, 3068),
        #(1000000000000, 1514285714288),
    )
)
def test_solve(n, expected):
    assert solve(MOVES, n) == expected

