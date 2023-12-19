import pytest

from .solution import find_arrangement_count_2, solve

DATA = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


def test_solve():
    assert solve(DATA) == 21


@pytest.mark.parametrize(
    'data,expected',
    (
        ("???.### 1,1,3", 1),
        #(".??..??...?##. 1,1,3", 4),
        #("?#?#?#?#?#?#?#? 1,3,1,6", 1),
        #("????.#...#... 4,1,1", 1),
        #("????.######..#####. 1,6,5", 4),
        #("?###???????? 3,2,1", 10),
    )
)
def test_find_arrangement_count(data, expected):
    assert find_arrangement_count_2(data) == expected