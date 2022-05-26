import pytest

from .solution import create_hash, densify, prepare_input, solve


@pytest.mark.parametrize(
    'size, lengths, expected',
    (
        (5, [1], [0, 1, 2, 3, 4]),
        (5, [3], [2, 1, 0, 3, 4]),
        (5, [3, 4], [4, 3, 0, 1, 2]),
        (5, [3, 4, 1], [4, 3, 0, 1, 2]),
        (5, [3, 4, 1, 5], [3, 4, 2, 1, 0]),
    )
)
def test_create_hash(size, lengths, expected):
    assert create_hash(size, lengths) == expected


@pytest.mark.parametrize(
    'data, repeats, expected',
    (
        ('1,2,3', 1, [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]),
        (
            '1,2,3',
            2,
            [49, 44, 50, 44, 51, 17, 31, 73, 47, 23, 49, 44, 50, 44, 51, 17, 31, 73, 47, 23],  # noqa
        ),
    )
)
def test_prepare_input(data, repeats, expected):
    assert prepare_input(data, repeats) == expected


def test_solve():
    assert solve('3,4,1,5', 5) == 12


@pytest.mark.parametrize(
    'data, expected',
    (
        ([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22], [64]),
    )
)
def test_densify(data, expected):
    assert densify(data) == expected
