import pytest

from .solution import code_generator, position_generator, solve


@pytest.mark.parametrize(
    'n, expected',
    (
        (1, 20151125),
        (2, 31916031),
        (3, 18749137),
    )
)
def test_code_generator(n, expected):
    cg = code_generator()
    while n:
        code = next(cg)
        n -= 1
    assert code == expected


@pytest.mark.parametrize(
    'n, expected',
    (
        (1, (1, 1)),
        (2, (1, 2)),
        (3, (2, 1)),
        (4, (1, 3)),
        (5, (2, 2)),
        (6, (3, 1)),
        (7, (1, 4)),
    )
)
def test_position_generator(n, expected):
    pg = position_generator()
    while n:
        position = next(pg)
        n -= 1
    assert position == expected


@pytest.mark.parametrize(
    'row, column, expected_code',
    (
        (1, 1, 20151125),
        (2, 1, 31916031),
        (1, 2, 18749137),
    )
)
def test_solve(row, column, expected_code):
    assert solve(row, column) == expected_code
