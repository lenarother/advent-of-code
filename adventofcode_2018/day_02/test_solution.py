import pytest

from .solution import solve, solve2

DATA = """
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
"""

DATA_2 = """
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
"""

EXAMPLES_2 = (
    ('abc\naxy', None),
    ('abc\naxc', 'ac'),
    (DATA_2, 'fgij'),
)


def test_solve():
    assert solve(DATA) == 12


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected
