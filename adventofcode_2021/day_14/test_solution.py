import pytest

from .solution import solve

DATA = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

EXAMPLES = (
    (DATA, 10, 1588),
    (DATA, 40, 2188189693529),
)


@pytest.mark.parametrize('data,steps,expected', EXAMPLES)
def test_solve(data, steps, expected):
    assert solve(data, steps) == expected
