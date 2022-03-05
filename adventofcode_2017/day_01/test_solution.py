import pytest

from .solution import solve, solve2

EXAMPLES = (
    ('1122', 3),
    ('1111', 4),
    ('1234', 0),
    ('91212129', 9),
)

EXAMPLES_2 = (
    ('1212', 6),
    ('1221', 0),
    ('123425', 4),
    ('123123', 12),
    ('12131415', 4),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected
