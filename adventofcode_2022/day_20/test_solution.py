import pytest

from .solution import solve, get_new_index, MovableInt, move_number

DATA = """
1
2
-3
3
-2
0
4
"""
"""
1, 2, -3, 3, -2, 0, 4

1 moves between 2 and -3:
2, 1, -3, 3, -2, 0, 4

2 moves between -3 and 3:
1, -3, 2, 3, -2, 0, 4

-3 moves between -2 and 0:
1, 2, 3, -2, -3, 0, 4

3 moves between 0 and 4:
1, 2, -2, -3, 0, 3, 4

-2 moves between 4 and 1:
1, 2, -3, 0, 3, 4, -2

0 does not move:
1, 2, -3, 0, 3, 4, -2

4 moves between -3 and 0:
1, 2, -3, 4, 0, 3, -2
"""


@pytest.mark.parametrize(
    'n, input_list, expected',
    (
        (
            1,
            [1, 2, -3, 3, -2, 0, 4],
            [2, 1, -3, 3, -2, 0, 4],
        ),
        (
            2,
            [2, 1, -3, 3, -2, 0, 4],
            [1, -3, 2, 3, -2, 0, 4],
        ),        (
            -3,
            [1, -3, 2, 3, -2, 0, 4],
            [1, 2, 3, -2, -3, 0, 4],
        ),
        (
            3,
            [1, 2, 3, -2, -3, 0, 4],
            [1, 2, -2, -3, 0, 3, 4],
        ),
        (
            -2,
            [1, 2, -2, -3, 0, 3, 4],
            [1, 2, -3, 0, 3, 4, -2],
        ),
        (
            0,
            [1, 2, -3, 0, 3, 4, -2],
            [1, 2, -3, 0, 3, 4, -2],
        ),
    )
)
def test_move_number(n, input_list, expected):
    input_list = [MovableInt(i) for i in input_list]
    n = MovableInt(n)
    assert move_number(n, input_list) == expected


def test_solve():
    assert solve(DATA) == 3


@pytest.mark.parametrize(
    'n, i, expected',
    (
        (1, 0, 1),
        (1, 0, 1),
    )
)
def test_get_new_index(n, i, expected):
    assert get_new_index(n, i) == expected
