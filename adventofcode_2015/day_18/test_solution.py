import pytest

from .solution import solve, solve2

DATA = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""

EXAMPLES = (
    (DATA, 4, 4),
)
EXAMPLES_2 = (
    (DATA, 0, {(0, 0), (0, 5), (5, 0), (5, 5)}, 17),
    (DATA, 1, {(0, 0), (0, 5), (5, 0), (5, 5)}, 18),
    (DATA, 5, {(0, 0), (0, 5), (5, 0), (5, 5)}, 17),
)


@pytest.mark.parametrize('data,steps,expected', EXAMPLES)
def test_solve(data, steps, expected):
    assert solve(data, steps) == expected


@pytest.mark.parametrize('data,steps,corners,expected', EXAMPLES_2)
def test_solve2(data, steps, corners, expected):
    assert solve2(data, steps, corners) == expected
