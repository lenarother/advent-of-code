import pytest

from .solution import is_valid, is_valid_strict


@pytest.mark.parametrize(
    'num, expected',
    (
        (111111, True),
        (223450, False),
        (123789, False),
    )
)
def test_is_valid(num, expected):
    assert is_valid(num) == expected


@pytest.mark.parametrize(
    'num, expected',
    (
        (112233, True),
        (123444, False),
        (111122, True),
    )
)
def test_is_valid_strict(num, expected):
    assert is_valid_strict(num) == expected
