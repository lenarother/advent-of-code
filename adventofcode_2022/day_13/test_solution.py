import pytest

from .solution import solve, compare_lists

DATA = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

def test_solve():
    assert solve(DATA) == 13


@pytest.mark.parametrize(
    'left, right, expected',
    (
        ('[1,1,3,1,1]', '[1,1,5,1,1]', True),
    )
)
def test_compare_pair(left, right, expected):
    assert compare_lists(left, right) == expected
