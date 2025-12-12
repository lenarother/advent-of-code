import pytest

from .solution import solve

DATA = """
0:
###
##.
#..

1:
##.
###
#.#

2:
..#
.##
##.

3:
###
#..
###

4:
#.#
###
#.#

5:
..#
###
###

41x48: 47 27 36 34 31 32
36x50: 46 53 35 41 46 53
43x42: 39 45 50 52 48 44
"""

EXAMPLES = (
    (DATA, 1),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected
