import pytest

from .solution import solve, sort_brisks

DATA = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

DATA_2 = """
1,1,8~1,1,9
2,0,5~2,2,5
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
0,1,6~2,1,6
"""

EXAMPLES = (
    (DATA, 5),
    (DATA_2, 5),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert 1 == 1
    assert solve(data) == expected


def test_sort_brisks():
    assert sort_brisks(DATA) == sort_brisks(DATA_2)
