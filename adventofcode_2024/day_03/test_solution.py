import pytest

from .solution import solve, solve2

DATA = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"  # noqa
DATA_2 = "xmul(1,444)%&mul"
DATA_3 = "xmul(1,4444)%&mul"
DATA_4 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"  # noqa

EXAMPLES = (
    (DATA, 161),
    (DATA_2, 444),
    (DATA_3, 0),
)

EXAMPLES_2 = (
    (DATA_4, 48),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve_2(data, expected):
    assert solve2(data) == expected
