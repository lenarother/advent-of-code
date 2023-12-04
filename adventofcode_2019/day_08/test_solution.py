import pytest

from .solution import solve

EXAMPLES = (
    ('123456789012', 3, 2, 1),
    ('122456789012', 3, 2, 2),
    ('122156789012', 3, 2, 4),
    ('789012122156', 3, 2, 4),
    ('000012122100', 3, 2, 4),
    ('0000000012122100', 5, 2, 4),
)

EXAMPLES_2 = (
    ('0222112222120000', 2, 2, '0110'),
    ('0000112222120000', 2, 2, '0000'),
)


@pytest.mark.parametrize('data,x,y,expected', EXAMPLES)
def test_solve(data, x, y, expected):
    assert solve(data, x, y) == expected


# @pytest.mark.parametrize('data,x,y,expected', EXAMPLES_2)
# def test_solve_2(data, x, y, expected):
#     assert solve_2(data, x, y) == expected
