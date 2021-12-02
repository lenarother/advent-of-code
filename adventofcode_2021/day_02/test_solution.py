import pytest

from .solution import solve, solve2

EXAMPLES = (
    ("""forward 5
down 5
forward 8
up 3
down 8
forward 2""", (15, 10)),
)

EXAMPLES2 = (
    ("""forward 5
down 5
forward 8
up 3
down 8
forward 2""", (15, 60)),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES2)
def test_solve2(data, expected):
    assert solve2(data) == expected
